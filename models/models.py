from dataclasses import dataclass
from datetime import datetime

@dataclass
class VatsimGeneral:
    version: str
    reload: str
    update: str             #will be used as a pk
    update_timestamp: str   #ISO 8601 date string in UTC
    connected_clients: int
    unique_users: int

    def get_datetime(self) -> datetime:
        """
        Uses the internal ISO 8601 timestamp to yield a date
        """
        return datetime.fromisoformat(self.update_timestamp)


@dataclass
class VatsimPilot:
    pass

@dataclass
class VatsimController:
    pass

@dataclass
class VatsimATIS:
    pass

@dataclass
class VatsimServer:
    pass

@dataclass
class VatsimFlightPlan:
    pass

@dataclass
class VatsimFacility:
    pass

@dataclass
class VatsimRating:
    pass

@dataclass
class VatsimPilotRating:
    pass

