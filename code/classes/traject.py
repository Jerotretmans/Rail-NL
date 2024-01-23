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
        # Initializeer het traject object, met een naam, een lijst stations en de totale tijd
        self.name = name
        self.stations_in_traject = []
        self.stations_in_traject_name_only = []
        self.station_counter = 0
        self.time = 0
        self.current_station = None
        
    
    def add_station(self, new_station) -> None:
        # als er nog geen station in de trajectlijst staat:
        if self.station_counter == 0:
            self.stations_in_traject.append(new_station)
            self.current_station = new_station
            self.station_counter += 1
        # als er wel een station in staat moet er worden gecheckt of er een verbinding bestaat tussen de stations
        else:
            # checkt voor nieuw station alle verbindingen
            for connected_station_name, time in new_station.connections.items():
                # als een van de verbindingen van nieuw station het huidige station is
                if connected_station_name == self.current_station.get_name():
                    # station toevoegen aan traject lijst
                    self.stations_in_traject.append(new_station)
                    # nieuw station wordt huidig station
                    self.current_station = new_station
                    time = int(time)
                    # totale trajecttijd wordt bij elkaar opgeteld
                    self.time += time
                    self.station_counter += 1
            #     else:
            #         print("geen verbinding tussen nieuw en huidig station")
                    
    def delete_station(self):
        current_station = self.stations_in_traject[self.station_counter - 1]

        for connected_station_name, time in current_station.connections.items():
            if self.stations_in_traject[self.station_counter - 2].get_name() == connected_station_name:
                del self.stations_in_traject[self.station_counter - 1]
                time = int(time)
                self.time -= time
                self.station_counter -= 1
                # print("station deleted")


    def get_name(self):
        return f"{self.name}"
    
    def get_names(self):
        station_names = []
        for station in self.stations_in_traject:
            station_names.append(station.get_name())
        return(station_names)
    
    def get_time(self):
        return self.time
    
    def __repr__(self):
        return f"{self.name}, {self.get_names()}"


if __name__ == "__main__":
    """
    Test functie voordat we in main.py bezig gaan.
    """

    # Lees verbindingen van CSV bestand
    connections = read_csv_file('../../data/ConnectiesHolland.csv')
    
    test_stations = []
    station1 = Station('Hoorn')
    station2 = Station('Alkmaar')
    station3 = Station('Den Helder')
    station4 = Station('Gouda')
    station5 = Station('Alkmaar')

    test_stations.append(station1)
    test_stations.append(station2)
    test_stations.append(station3)
    test_stations.append(station4)
 

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
    
    print(traject1.get_names())



    
