import sys
sys.path.append('../')
from helpers import read_csv_file

class Station:
    def __init__(self, name, y, x,):
        self.name = name
        self.y = y
        self.x = x
        self.connections = {}

    def create_connections(self):
        connections = read_csv_file('../../data/ConnectiesHolland.csv')
        for row in connections:
            station1 = row[0]
            station2 = row[1]
            time = row[2]
            print(station1, station2, time)
            if station1 == self.name:
                self.connections[station2] = time
            elif station2 == self.name:
                self.connections[station1] = time
                    

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
    
    # for station in station_objects:
    #     print(f"Station: {station.name}, Connections: {station.connections}")