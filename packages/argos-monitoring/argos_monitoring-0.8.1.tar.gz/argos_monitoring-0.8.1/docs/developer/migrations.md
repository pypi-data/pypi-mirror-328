---
description: How to use Alambic to add a database migratation to Argos.
---
# Adding a database migration

We are using [Alembic](https://alembic.sqlalchemy.org) to handle the database
migrations. Here is how to proceed in order to add a new migration:

First, do your changes in the code, change the model, add new tables, etc. Once
you're done, you can create a new migration.

```bash
venv/bin/alembic -c argos/server/migrations/alembic.ini revision \
    --autogenerate -m "migration reason"
```

Edit the created file to remove comments and adapt it to make sure the migration is complete (Alembic is not powerful enough to cover all the corner cases).

In case you want to add an `Enum` type and use it in an existing table, please have a look at [`argos/server/migrations/versions/dcf73fa19fce_specify_check_method.py`](https://framagit.org/framasoft/framaspace/argos/-/blob/main/argos/server/migrations/versions/dcf73fa19fce_specify_check_method.py).

If you want to add an `Enum` type in a new table, you can do like in [`argos/server/migrations/versions/7d480e6f1112_initial_migrations.py`](https://framagit.org/framasoft/framaspace/argos/-/blob/main/argos/server/migrations/versions/7d480e6f1112_initial_migrations.py)
