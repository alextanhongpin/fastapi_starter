# fastapi guide

```bash
# To start the server.
$ make start
```

## Pipenv

```bash
$ pipenv shell
$ pipenv install <package>

# Installing dev only dependencies.
$ pipenv install <package> --dev
```

## Database

Using SQLAlchemy with Alembic.

```bash
$ alembic init alembic/

# Create new migration file.
$ make sql-'create table xyz'

# Run migration
$ make migrate

# Reset all migration
$ make rollback
```

## Subapis

```bash
# For root docs.
$ open http://localhost:8000/docs

# For users docs.
$ open http://localhost:8000/users/docs
```
