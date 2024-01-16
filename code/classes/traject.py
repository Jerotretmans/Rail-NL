from stations import Station
import sys
sys.path.append('../')
from helpers import read_csv_file

class Traject:
    """
    Returnt een lijst met namen van stations die aan elkaar verbonden zijn.
    Telt de totale duur van het traject op. 

    Constraint: max 120 min per traject
    """
    
    def __init__(self, name) -> None:
        self.name = name
        self.stations_in_traject = []
        self.station_counter = 0
        self.time = 0
        self.current_station = None
        
    
    def add_station(self, new_station) -> None:
        if self.station_counter == 0:
            self.stations_in_traject.append(station)
            self.current_station = new_station
            self.station_counter += 1
        else:
            # for connected_station_name, time in station.connections.items():
            print("succes")
            if station.get_name in self.current_station.connections:
                print("succes2")

                # connection exists & station can be added to track.        

        # print(station.connections.items())
        for stations_with_connection, time in station.connections.items():
            print(f"1: {station.get_name()}")
            print(f"2: {stations_with_connection}")
            
            # if station.get_name()  stations_with_connection:
            #     self.stations_in_traject.append(station)
            #     self.time += int(time)

    def __repr__(self):
        return f"{self.name}: {self.stations_in_traject}, Time: {self.time}"


if __name__ == "__main__":
    """
    Test functie voordat we in main.py bezig gaan.
    """

    connections = read_csv_file('../../data/ConnectiesHolland.csv')
    # print(connections)
    
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
    
    name = "Track1"
    traject1 = Traject(name)
    
    for station in test_stations:
        print(f"Name: {station.get_name()}")
        traject1.add_station(station)
    
    # print(traject1)



    
