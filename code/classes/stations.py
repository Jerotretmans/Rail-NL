"""
Bevat de namen en locaties van stations samen met een dictionary met alle 
connecties van de stations.
"""

class Station:

    def __init__(self, name: str) -> None:
        self.name = name
        self.connections= {}
        self.locations = {}

    # Voeg connecties toe met bijbehorende tijd
    def create_connection(self, other_station: str, time: int) -> None:
        self.connections[other_station] = time

    # Voeg de coördinaten van de stations toe
    def add_location(self, x: float, y: float) -> None:
        self.locations[self.name] = [x, y]

    # Check of er een verbinding is met een bepaald station
    def has_connection(self, other_station) -> bool:
        if other_station in self.connections:
            return True
        else:
            return False
    
    # Return de naam van een station
    def get_name(self) -> str:
        return self.name
