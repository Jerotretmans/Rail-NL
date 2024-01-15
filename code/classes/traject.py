from stations import Station
import sys
sys.path.append('../')
from helpers import read_csv_file

class Traject:
    def __init__(self, name):
        self.name = name
        self.stations_in_traject = []
        self.time = 0
    
    def add_station(self, station):
        self.stations_in_traject.append(station)
        for connected_station, time in station.connections.items():
            self.time += time

    def print_stations_details(self):
        print(f"Details for Traject {self.name}:")
        for station in self.stations_in_traject:
            print(f"Station {station.name}:")
            print(f" - Name: {station.name}")
            print(f" - Connections: {station.connections}")


if __name__ == "__main__":

    connections = read_csv_file('../../data/ConnectiesHolland.csv')
    
    test_stations = []
    station1 = Station('Hoorn')
    station2 = Station('Alkmaar')
    test_stations.append(station1)
    test_stations.append(station2)

    for row in connections:
        main_station = row[0]
        connected_station = row[1]
        time = row[2]

        for station in test_stations:
            if station.name == main_station:
                station.create_connection(connected_station, time)
            elif station.name == connected_station:
                station.create_connection(main_station, time)
    
    name = "traject1"
    traject1 = Traject(name)
    
    for station in test_stations:
        station.print_station_name()
        traject1.add_station(station)
        
    # traject1.print_stations_details()

    # print(f"{traject1.name}, {traject1.stations}")


    
