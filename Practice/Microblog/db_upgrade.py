__author__ = 'Stuart'
"""
Why record db migrations?

Let's say that for the next release of your app you have to introduce a change to your models, for example a new table
needs to be added. Without migrations you would need to figure out how to change the format of your database, both in
your development machine and then again in your server, and this could be a lot of work.

If you have database migration support, then when you are ready to release the new version of the app to your production
 server you just need to record a new migration, copy the migration scripts to your production server and run a simple
 script that applies the changes for you.

With this...

DB will be upgraded to latest revision, by applying migration scripts in db repo
"""

#!flask/scripts/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' +str(v))
