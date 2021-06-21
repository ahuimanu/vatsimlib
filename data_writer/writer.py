"""
Will write to database using SQL Alchemy

example pulls from the tutorial
"""

from importlib import resources

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models.models import VatsimGeneral
from models.mapped_models import do_mapping

# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine("sqlite:///vatsimdata.db")

# do_mapping()
