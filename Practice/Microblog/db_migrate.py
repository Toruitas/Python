__author__ = 'Stuart'
#!flask/bin/python

"""
Compares structure of app.db against structure of app/models.py. Difference between the two recorded as migration script
inside migration repository. Then migration script can apply migration or undo - upgrade or downgrade.

Protip: never rename existing fields, and limit changes to adding or removing models or fields, or changing types
of existing fields. And always review the generated migration script.

This will also record the version of the database.
"""

import types
from migrate.versioning import api
from app import db
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO

v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)  # gets current version
migration = SQLALCHEMY_MIGRATE_REPO + ('/versions/%03d_migration.py' % (v+1))  # string name for migration file
tmp_module = types.ModuleType('old model')  # creates empty model for temp
old_model = api.create_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)  #

exec(old_model,tmp_module.__dict__)
script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO, tmp_module.meta,db.metadata)

open(migration,"wt").write(script)
api.upgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
print("New migration saved as "+ migration)
print("Current database version: "+ str(v))