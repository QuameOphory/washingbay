from dataclasses import dataclass, field
from clients import Client

@dataclass
class Vehicle:

    _vehicles_list = None

    brand: str
    model: str
    registration_number: str
    owner: Client

    def __post_init__(self):
        self.washed = False

    def wash(self) -> None:
        self.washed = True

    @staticmethod
    def get_vehicles_list():
        if Vehicle._vehicles_list == None:
            Vehicle._vehicles_list = []
        return Vehicle._vehicles_list
