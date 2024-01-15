from stations import Station
import sys
sys.path.append('../')
from helpers import read_csv_file

class Traject:
    def __init__(self, name):
        self.name = name
        self.stations = []
        # self.time = 0
    
    def add_station(self, other_station):
        self.stations.append(other_station)

    # def get_connection(self, other_station):
    #     return self.stations.name
    
    # def get_time(self, other_station):
    #     return self.stations[other_station.time]


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
            if station1.name == main_station:
                station1.create_connection(connected_station, time)
            elif station1.name == connected_station:
                station1.create_connection(main_station, time)


    traject1 = Traject(station1)
    traject1.add_station(station)

    print(f"{traject1.name}, {traject1.stations}")


    
