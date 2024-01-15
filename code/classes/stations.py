import sys
sys.path.append('../')
from helpers import read_csv_file

class Station:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def create_connection(self, other_station, time):
        self.connections[other_station] = time

    def get_connection(self, other_station):
        if other_station in self.connections:
            return True
        else:
            return False
        
    def get_name(self):
        return self.name
        

if __name__ == "__main__":
    stations = read_csv_file('../../data/StationsHolland.csv')
    connections = read_csv_file('../../data/ConnectiesHolland.csv')
    
    station_objects = []
    for row in stations:
        name = row[0]
        station = Station(name)
        station_objects.append(station)

    for row in connections:
        main_station = row[0]
        connected_station = row[1]
        time = row[2]

        for station in station_objects:
            if station.name == main_station:
                station.create_connection(connected_station, time)
            elif station.name == connected_station:
                station.create_connection(main_station, time)   
    
    for station in station_objects:
        print(f"Station: {station.name}, Connections: {station.connections} \n")