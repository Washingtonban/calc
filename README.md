# Education Projetc calc

# Install psycopg2 in Mac M1
Error while installing through `pip install psycopg2` looks like this:

```
Please add the directory containing pg_config to the PATH

or specify the full executable path with the option (...)
```

Reference to the solution [here](https://stackoverflow.com/questions/66888087/cannot-install-psycopg2-with-pip3-on-m1-mac).

## Steps followed in my local

Install PostgreSQL, start the deamon and install `openssl`:

```
brew install postgresql
pg_ctl -D /opt/homebrew/var/postgres start
brew install openssl
```

If you already have `openssl` installed, run:

```
brew reinstall openssl
```

Find the path of `pg_config` and `openssl`:

```
which pg_config
which openssl
```

In my case those were located in these folders:

```
/opt/homebrew/Cellar/postgresql/13.3/bin/pg_config
/opt/homebrew/Cellar/openssl@1.1/1.1.1k/bin/openssl
```

Add that to `$PATH`:

```
export PATH=$PATH:/opt/homebrew/Cellar/postgresql/13.3/bin/pg_config
export PATH=$PATH:/opt/homebrew/Cellar/openssl@1.1/1.1.1k/bin/openssl
```

Then run: `pip install psycopg2`.

## Problems while executing django command
I encountered the following error while running a django command:

```
Traceback (most recent call last):
  File "/Users/user/opt/miniconda3/envs/dat/lib/python3.7/site-packages/django/db/backends/postgresql/base.py", line 25, in <module>
    import psycopg2 as Database
  File "/Users/user/opt/miniconda3/envs/dat/lib/python3.7/site-packages/psycopg2/__init__.py", line 51, in <module>
    from psycopg2._psycopg import (                     # noqa
ImportError: dlopen(/Users/user/opt/miniconda3/envs/dat/lib/python3.7/site-packages/psycopg2/_psycopg.cpython-37m-darwin.so, 2): Symbol not found: _PQbackendPID
  Referenced from: /Users/user/opt/miniconda3/envs/dat/lib/python3.7/site-packages/psycopg2/_psycopg.cpython-37m-darwin.so
  Expected in: flat namespace
 in /Users/user/opt/miniconda3/envs/dat/lib/python3.7/site-packages/psycopg2/_psycopg.cpython-37m-darwin.so
```

Following [this thread](https://github.com/psycopg/psycopg2/issues/1216), this finally worked:

```
brew install libpq --build-from-source
export LDFLAGS="-L/opt/homebrew/opt/libpq/lib"
pip install psycopg2-binary
```

Before using that, uninstall `psycopg2` and `psycopg2-binary`:

```
pip uninstall psycopg2-binary
pip uninstall psycopg2
```