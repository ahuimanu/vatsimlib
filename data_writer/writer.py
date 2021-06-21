"""
Will write to database using SQL Alchemy

example pulls from the tutorial
"""

from importlib import resources

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm.session import sessionmaker

from models.models import VatsimGeneral
from models.mapped_models import do_mapping

# sqlite://<nohostname>/<path>
# where <path> is relative:

engine, session = None


def prep():

    with resources.path("vatsimlib.data", "vatsim.db") as sqlite_filepath:
        engine = create_engine("sqlite:///vatsimdata.db")

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    do_mapping()


def add_vatsim_general():
    # read using reader
    # write to db
    pass


def write():
    prep()
    add_vatsim_general()
