# fastapi guide

```bash
# To start the server.
$ make start
```

## Pipenv


### Install.

```bash
$ pip install --user pipenv
```

If pipenv is not found, add the following to your .bashrc or .zshrc
```
export PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"
export PATH="$PATH:$PYTHON_BIN_PATH"
```

### Usage

Basic usage:

```bash
$ pipenv shell
$ pipenv install <package>

# Installing dev only dependencies.
$ pipenv install <package> --dev
```

If it still doesn't work, run this:

```bash
$ python3 -m pip install pipenv
$ python3 -m pipenv shell
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
