# Using testcontainers for python

During testing, we need to setup a test database using Docker.

https://github.com/testcontainers/testcontainers-python


Installation:

```bash
$ pipenv install --dev testcontainers
```

```python
>>> from testcontainers.postgres import PostgresContainer
>>> import sqlalchemy

>>> with PostgresContainer("postgres:9.5") as postgres:
...     engine = sqlalchemy.create_engine(postgres.get_connection_url())
...     result = engine.execute("select version()")
...     version, = result.fetchone()
>>> version
'PostgreSQL 9.5...'
```
