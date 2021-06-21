import requests
from models.models import VatsimGeneral, VatsimPilot


def init():
    response = requests.get("https://data.vatsim.net/v3/vatsim-data.json")
    return response.json()


def get_vatsim_general(json_data):
    # https://pynative.com/python-convert-json-data-into-custom-python-object/
    if json_data:
        return VatsimGeneral(**json_data["general"])


def get_vatsim_pilots(json_data):
    if json_data:
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        pilots = [p for p in json_data["pilots"] if VatsimPilot(**p)]
        return pilots
