import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi_utils.tasks import repeat_every
from psutil import Process
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from argos.logging import logger, set_log_level
from argos.server import models, routes, queries
from argos.server.alerting import no_agent_alert
from argos.server.exceptions import NotAuthenticatedException, auth_exception_handler
from argos.server.settings import read_config


def get_application() -> FastAPI:
    """Spawn Argos FastAPI server"""
    config_file = os.environ["ARGOS_YAML_FILE"]
    config = read_config(config_file)

    root_path = config.general.root_path

    if root_path != "":
        logger.info("Root path for Argos: %s", root_path)
        if root_path.endswith("/"):
            root_path = root_path[:-1]
            logger.info("Fixed root path for Argos: %s", root_path)

    appli = FastAPI(lifespan=lifespan, root_path=root_path)

    # Config is the argos config object (built from yaml)
    appli.state.config = config
    appli.add_exception_handler(NotAuthenticatedException, auth_exception_handler)
    appli.state.manager = create_manager(config.general.cookie_secret)

    if config.general.ldap is not None:
        import ldap

        appli.state.ldap = ldap.initialize(config.general.ldap.uri)

    @appli.state.manager.user_loader()
    async def query_user(user: str) -> None | str | models.User:
        """
        Get a user from the db or LDAP
        :param user: name of the user
        :return: None or the user object
        """
        if appli.state.config.general.ldap is not None:
            from argos.server.routes.dependencies import find_ldap_user

            return await find_ldap_user(appli.state.config, appli.state.ldap, user)

        return await queries.get_user(appli.state.db, user)

    appli.include_router(routes.api, prefix="/api")
    appli.include_router(routes.views)

    static_dir = Path(__file__).resolve().parent / "static"

    appli.mount("/static", StaticFiles(directory=static_dir), name="static")
    return appli


async def connect_to_db(appli):
    appli.state.db = appli.state.SessionLocal()
    return appli.state.db


def setup_database(appli):
    config = appli.state.config
    db_url = str(config.general.db.url)
    logger.debug("Using database URL %s", db_url)
    # For sqlite, we need to add connect_args={"check_same_thread": False}
    if config.general.env == "production" and db_url.startswith("sqlite:////tmp"):
        logger.warning("Using sqlite in /tmp is not recommended for production")

    extra_settings = {}
    if config.general.db.pool_size:
        extra_settings.setdefault("pool_size", config.general.db.pool_size)

    if config.general.db.max_overflow:
        extra_settings.setdefault("max_overflow", config.general.db.max_overflow)

    engine = create_engine(db_url, **extra_settings)

    def _fk_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute("pragma foreign_keys=ON")

    if db_url.startswith("sqlite:///"):
        event.listen(engine, "connect", _fk_pragma_on_connect)

    appli.state.SessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    appli.state.engine = engine
    models.Base.metadata.create_all(bind=engine)


def create_manager(cookie_secret: str) -> LoginManager:
    if cookie_secret == "foo_bar_baz":
        logger.warning(
            "You should change the cookie_secret secret in your configuration file."
        )
    return LoginManager(
        cookie_secret,
        "/login",
        use_cookie=True,
        use_header=False,
        not_authenticated_exception=NotAuthenticatedException,
    )


@repeat_every(seconds=120, logger=logger)
async def recurring_tasks() -> None:
    """Recurring DB cleanup and watch-agents tasks"""
    # If we are using gunicorn
    if not hasattr(app.state, "SessionLocal"):
        parent_process = Process(os.getppid())
        children = parent_process.children(recursive=True)
        # Start the task only once, not for every worker
        if children[0].pid == os.getpid():
            # and we need to setup database engine
            setup_database(app)
        else:
            return None

    set_log_level("info", quiet=True)
    logger.info("Start background recurring tasks")

    with app.state.SessionLocal() as db:
        config = app.state.config.recurring_tasks

        agents = await queries.get_recent_agents_count(db, config.time_without_agent)
        if agents == 0:
            no_agent_alert(app.state.config)
        logger.info("Agent presence checked")

        removed = await queries.remove_old_results(db, config.max_results_age)
        logger.info("%i result(s) removed", removed)

        updated = await queries.release_old_locks(db, config.max_lock_seconds)
        logger.info("%i lock(s) released", updated)

        processed_jobs = await queries.process_jobs(db)
        logger.info("%i job(s) processed", processed_jobs)

    logger.info("Background recurring tasks ended")

    return None


@asynccontextmanager
async def lifespan(appli: FastAPI):
    """Server start and stop actions

    Setup database connection then close it at shutdown.
    """
    setup_database(appli)

    db = await connect_to_db(appli)

    tasks_count = await queries.count_tasks(db)
    if tasks_count == 0:
        logger.warning(
            "There is no tasks in the database. "
            'Please launch the command "argos server reload-config"'
        )
    await recurring_tasks()

    yield

    appli.state.db.close()


app = get_application()
