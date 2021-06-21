from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import List

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import registry, relationship

from .models import VatsimGeneral, VatsimPilot, VatsimFlightPlan, VatsimServer

# references:

# https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-a-k-a-classical-mappings
# https://realpython.com/python-sqlite-sqlalchemy/#working-with-sqlalchemy-and-python-objects

mapper_registry = registry()

metadata = MetaData()

def do_mapping():

    # "version": 1,
    # "reload": 1,
    # "update": "20201108045351",
    # "update_timestamp": "2020-11-08T04:53:51.941524Z",
    # "connected_clients": 482,
    # "unique_users": 461

    # mapping for the vatsim general table
    vatsim_general = Table(
        "vatsim_general",
        metadata,
        Column("update", String(14), primary_key=True),
        Column("version", Integer),
        Column("reload", Integer),
        Column("update_timestamp", String(27)),
        Column("connected_clients", Integer),
        Column("unique_users", Integer),
    )

    mapper_registry.map_imperatively(VatsimGeneral, vatsim_general)
