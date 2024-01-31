import sys
from typing import Dict, List, Tuple
sys.path.append('../')
from helpers import read_csv_file

class Station:
    """
    Bevat de naam van stations en een dictionary met alle connecties van de stations.
    """

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
        

if __name__ == "__main__":
    """
    Test functie voordat we in main.py bezig gaan.
    """

    # Lees de locatie en connecties tussen stations vanuit csv bestanden
    stations = read_csv_file('../../data/StationsHolland.csv')
    connections = read_csv_file('../../data/ConnectiesHolland.csv')
    
    # Maak stations objecten voor elk station in de csv bestanden
    station_objects = []
    for row in stations:
        name: str = row[0]
        station = Station(name)
        station_objects.append(station)
        x: float = row[2]
        y: float = row[1]
        station.add_location(x, y)
        

    # Maak de verbindingen tussen stations uit het csv bestand en onthoud de tijd voor elke verbinding
    for row in connections:
        main_station = row[0]
        connected_station = row[1]
        time = row[2]

        for station in station_objects:
            if station.name == main_station:
                station.create_connection(connected_station, time)
            elif station.name == connected_station: # Garandeert unieke stations, geen dubbelen
                station.create_connection(main_station, time)

    # for station in station_objects:
    #     print(station.has_connection('Hoorn')) 
    
    # Print de details voor elk station (Lijst van alle connecties en bijbehorende tijd)
    for station in station_objects:
        print(f"Station: {station.name}, Location: {station.locations}, Connections: {station.connections} \n")