import sys
from typing import Dict, List, Tuple
sys.path.append('../')
from helpers import read_csv_file

"""
Bevat de naam van stations en een dictionary met alle connecties van de stations.
"""

class Station:

    def __init__(self, name: str):
        # Initialize een station object met een naam en mogelijke verbindingen
        self.name: str = name
        self.connections: Dict[str, str]= {}
        self.locations: Dict[str, Tuple[float, float]] = {}

    def create_connection(self, other_station: str, time: int) -> None:
        # Maak de verbindingen met stations met een bepaalde tijd
        self.connections[other_station] = time

    def add_location(self, x: float, y: float) -> None:
        # Voeg de coördinaten van de stations toe
        self.locations[self.name] = [x, y]

    def has_connection(self, other_station: str) -> bool:
        # Check of er een verbinding is met een bepaald station
        if other_station in self.connections:
            return True
        else:
            return False
        
    def get_name(self)-> str:
        # Krijg de naam van een station
        return self.name
