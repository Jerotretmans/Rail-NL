import sys
sys.path.append('../classes')

from classes.stations import Station


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
        self.max_tijd: int
        
    
    def add_station(self, new_station) -> None:
        # als er nog geen station in de trajectlijst staat:
        if self.station_counter == 0:
            self.stations_in_traject.append(new_station)
            self.stations_in_traject_name_only.append(new_station.get_name())
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
                    self.stations_in_traject_name_only.append(new_station.get_name())
                    # nieuw station wordt huidig station
                    self.current_station = new_station
                    time = int(time)
                    # totale trajecttijd wordt bij elkaar opgeteld
                    self.time += time
                    self.station_counter += 1
            #     else:
            #         print("geen verbinding tussen nieuw en huidig station")
                    
    def delete_station(self):
        self.current_station = self.stations_in_traject[self.station_counter - 2]

        for connected_station_name, time in self.current_station.connections.items():
            if self.stations_in_traject[self.station_counter - 2].get_name() == connected_station_name:
                del self.stations_in_traject[self.station_counter - 1]
                del self.stations_in_traject_name_only[self.station_counter - 1]

                time = int(time)
                self.time -= time
                self.station_counter -= 1
                # print("station deleted")    
