from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from builtins import *

import os
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Sets connection string
conn_string = os.environ['SMARTMENDRDB'] if 'SMARTMENDRDB' in os.environ and os.environ['SMARTMENDRDB'] != '' \
    else 'sqlite:///' + os.getcwd() + os.sep + 'smartmendr.db'


# Sets global variable indicating whether we are using Postgres
smartmendr_postgres = conn_string.startswith('postgres')


# Automatically turns on foreign key enforcement for SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if conn_string.startswith('sqlite'):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


# Defines procedure for setting up a sessionmaker
def new_sessionmaker():
    
    # Turning on autocommit for Postgres, see http://oddbird.net/2014/06/14/sqlalchemy-postgres-autocommit/
    # Otherwise any e.g. query starts a transaction, locking tables... very bad for e.g. multiple notebooks
    # open, multiple processes, etc.
    if smartmendr_postgres:
        smartmendr_engine = create_engine(conn_string, isolation_level="AUTOCOMMIT")
    else:
        smartmendr_engine = create_engine(conn_string)

    # New sessionmaker
    smartmendrSession = sessionmaker(bind=smartmendr_engine)
    return smartmendrSession


# We initialize the engine within the models module because models' schema can depend on
# which data types are supported by the engine
smartmendrSession = new_sessionmaker()
smartmendr_engine = smartmendrSession.kw['bind']

smartmendrBase = declarative_base(name='smartmendrBase', cls=object)
