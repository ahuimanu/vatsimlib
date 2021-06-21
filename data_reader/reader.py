import json
import requests
from models.models import VatsimGeneral, VatsimPilot, VatsimFlightPlan

def init():
    response = requests.get("https://data.vatsim.net/v3/vatsim-data.json")
    return response.json()

def outlook(json_data):
    pilot = VatsimPilot(**json_data['pilots'][0])
    print(pilot)

def get_vatsim_general(json_data):
    # https://pynative.com/python-convert-json-data-into-custom-python-object/
    if json_data:
        return VatsimGeneral(**json_data["general"])

def get_pilot(pilot_data):
    pilot = VatsimPilot(**pilot_data)
    return pilot

def get_vatsim_pilots(json_data):
    if json_data:
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        pilots = []
        for p in json_data['pilots']:
            pilots.append(get_pilot(p))
        
        return pilots

def get_flight_plan_for_pilot(pilot):

    if pilot.flight_plan is not None:
        flight_plan = VatsimFlightPlan
        (
            pilot.flight_plan['flight_rules'],
            pilot.flight_plan['aircraft'],
            pilot.flight_plan['aircraft_faa'],
            pilot.flight_plan['aircraft_short'],
            pilot.flight_plan['departure'],
            pilot.flight_plan['arrival'],
            pilot.flight_plan['alternate'],
            pilot.flight_plan['cruise_tas'],
            pilot.flight_plan['altitude'],
            pilot.flight_plan['deptime'],
            pilot.flight_plan['enroute_time'],
            pilot.flight_plan['fuel_time'],
            pilot.flight_plan['remarks'],
            pilot.flight_plan['route'],
        )
        return flight_plan

    else:
        return None


def get_flight_plans(pilots):
    if(pilots):
        flight_plans = []
        for p in pilots:
            flight_plans.append(get_flight_plan_for_pilot(p))
    
    return flight_plans
