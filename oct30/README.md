# Notes for the tools and Stack

## `asyncio` :white_check_mark:


asyc libarary for python.    oesn't support event loop nesting.

**Docs Link** : `https://docs.python.org/3/library/asyncio.html`

## `asyncpg` :white_check_mark:

async wrapper for psql

**Docs Link** : `https://magicstack.github.io/asyncpg/current/`

## `psycopg2` :o:

Wrapper in Python for the Psql

**Docs Link** : `https://www.psycopg.org/docs/`

Cheatsheet:
```python
import psycopg2 as pg

conn = pg.connect("dbname=harrykd user=postgres")

cur = conn.cursor()

cur.execute("SELECT * from notes")

# fetch all records from table
records = cur.fetchall()

#fetch one record
rd = cur.fetchone()

# Commit changes
conn.commit()

# Communication with database
cur.close()
conn.close()
```

The maine entry points of psycopg are:

- `connect()` method --> creates a new db session and return connect instance

- The `connection` class --> holds db session and can create new cursor instance using `cursor()` method for queries and commands. Also terminates transactions with `commit()`or `rollback`

- The `cursor` class --> sends command to db using methods like `execute()` and `executemany()` . Can retreive data from db by iteration or using methods like `fetchone()`, `fetchmany()`, `fetchall()`



>> Notes:
>> Doesn't work as psycopg in my machine.
>> Use `import psycopg2`


## `pre-commit` :white_check_mark:

git hooks wrapper, supports plugins and custom hooks

**Docs Link** : `https://www.postgresql.org/docs`



## `psql` :o2:
PostreSQL for databases

**Docs Link** : `https://www.postgresql.org/docs`

## doctest

A module to search and run code examples in pieces of text and run python interactive Python sessions.

**D** : `https://docs.python.org/3/library/doctest.html#module-doctest`