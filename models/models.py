from dataclasses import dataclass
from datetime import datetime


@dataclass
class VatsimGeneral:
    version: str
    reload: str
    update: str  # will be used as a pk
    update_timestamp: str  # ISO 8601 date string in UTC
    connected_clients: int
    unique_users: int

    def get_datetime(self) -> datetime:
        """
        Uses the internal ISO 8601 timestamp to yield a date
        """
        return datetime.fromisoformat(self.update_timestamp)


@dataclass
class VatsimPilot:
    cid: str  # 1234567
    name: str  # JOE BLOGGS
    callsign: str  # AFR105
    server: str  # GERMANY-1
    pilot_rating: str  # 0
    latitude: float  # 46.28281
    longitude: float  # -53.40947
    altitude: int  # 34163
    groundspeed: int  # 424
    transponder: str  # 7630
    heading: int  # 252
    qnh_i_hg: float  # 30.08
    qnh_mb: int  # 1019
    logon_time: str  # "2020-11-28T18:43:02.8458311Z"
    last_updated: str  # "2020-11-28T22:42:59.9044667Z"


@dataclass
class VatsimFlightPlan:
    flight_rules: str  # I
    aircraft: str  # B77W/H-SDE1E2E3FGHIJ2J3J4J5M1RWXY/LB1D1
    aircraft_faa: str  # H/B77W/L
    aircraft_short: str  # B77W
    departure: str  # LFPG
    arrival: str  # KJFK
    alternate: str  # KBOS
    cruise_tas: int  # 470
    altitude: int  # 34000
    deptime: str  # 1410
    enroute_time: str  # 0735
    fuel_time: str  # 0942
    remarks: str  # "PBN/A1B1C1D1L1O1S2 DOF/201128 REG/FGZNE EET/EGTT0041 EISN0102 EGGX0136 52N020W0201 CZQX0250 49N040W0344 47N050W0442 CZQM0525 KZBW0635 KZNY0727 OPR/AF PER/D RALT/EGPO LPPD CYYT RMK/TCAS SIMBRIEF /V/",
    route: str  # "EVX4H/08L EVX DCT RUBIX DCT SENLO DCT JSY DCT LIZAD DCT NAKID DCT LND M142 INSUN DCT LESLU DCT XETBO DCT LIMRI/M083F350 NATA 47N050W/N0478F350 NATA PORTI/N0470F360 N170A BRADD DCT PLYMM PARCH3"

    def __str__(self) -> str:
        return f"{self.aircraft_faa}"


@dataclass
class VatsimController:
    pass


@dataclass
class VatsimATIS:
    pass


@dataclass
class VatsimServer:
    ident: str  # UK-1
    hostname_or_ip: str  # 209.97.177.84
    location: str  # London, UK
    name: str  # UK-1
    clients_connection_allowed: str  # 1


@dataclass
class VatsimFacility:
    pass


@dataclass
class VatsimRating:
    pass


@dataclass
class VatsimPilotRating:
    pass
