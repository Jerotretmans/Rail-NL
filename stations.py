import csv

class Station:
    def __init__(self, name, y, x,):
        self.name = name
        self.y = y
        self.x = x
        self.connections = {}
    
    def create_connections(self):
        with open('ConnectiesHolland.csv') as connections_file:
            connections = csv.reader(connections_file)
            header = next(connections)
            for row in connections:
                station1 = row[0]
                station2 = row[1]
                time = row[2]
                if station1 == self.name:
                    self.connections[station2] = time
                elif station2 == self.name:
                    self.connections[station1] = time
                    

if __name__ == "__main__":
    rows = []
    station_objects = []
  
    with open('StationsHolland.csv') as stations_file:
        stations = csv.reader(stations_file)
        header = next(stations)
        for row in stations:
            name = row[0]
            y = row[1]
            x = row[2]
            station = Station(name, y, x)
            station_objects.append(stations)

    # with open('ConnectiesHolland.csv') as connections_file:
    #     connections = csv.reader(connections_file)
    #     header = next(connections)
    #     for row in connections:
    #         station1 = row[0]
    #         station2 = row[1]
    #         time = row[2]
    #         stations = Station
    #         stations.connections(station1, station2, time)
    #         station_objects.append(stations)

    print(station_objects)

    # for station in station_objects:
    #     print(f"Station: {station.name}, Connections: {station.connections}")
