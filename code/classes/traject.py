from stations import Station
import sys
sys.path.append('../')
from helpers import read_csv_file

class Traject:
    def __init__(self):
        self.name = name
        self.stations = []
    
    def create_traject(self):
        pass

        
if __name__ == "__main__":
    stations = read_csv_file('../../data/StationsHolland.csv')
    station_objects = []
    
    for row in stations:
        name = row[0]
        y = row[1]
        x = row[2]

        station = Station(name, y, x)
        station.create_connections()
        station_objects.append(station)
    
    for station in station_objects:
        print(f"Station: {station.name}, Connections: {station.connections}")
