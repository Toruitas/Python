__author__ = 'Stuart'
"""
like upgrade, but down!
"""

#!flask/scripts/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)  # gets current db version
api.downgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO, v-1)  # downgrades to the last version
v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)  # stores current version, prints it
print('Current database version: ' +str(v))
