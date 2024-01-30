import sys
from typing import List, Optional
sys.path.append('../classes')

from classes.stations import Station


class Traject:
    """
    Returnt een lijst met namen van stations die aan elkaar verbonden zijn.
    Telt de totale duur van het traject op. 

    Constraint: max 120 min per traject
    """
    
    def __init__(self, name: str) -> None:
        # Initializeer het traject object, met een naam, een lijst stations en de totale tijd
        self.name: str = name
        self.stations_in_traject: List[Station] = []
        self.stations_in_traject_name_only: List[str] = []
        self.station_counter: int = 0
        self.time: int = 0
        self.current_station: Optional[Station] = None
        
    
    def add_station(self, new_station: Station) -> None:
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
                    time: int = int(time)
                    # totale trajecttijd wordt bij elkaar opgeteld
                    self.time += time
                    self.station_counter += 1
            #     else:
            #         print("geen verbinding tussen nieuw en huidig station")
                    
    def delete_station(self) -> None:
        # print(f"current station: {self.current_station.name}")
        # print(self.current_station.connections)
        # print(f"station counter: {self.station_counter}")
        station_to_delete = self.stations_in_traject.pop()
        self.stations_in_traject_name_only.pop()
        # print(f"deleted station: {station_to_delete.name}")
        self.station_counter = len(self.stations_in_traject)
        # print(f"station counter: {self.station_counter}")
        index_new = self.station_counter - 1
        station_next_to_it = self.stations_in_traject[index_new].name
        # print(f"station next to it: {station_next_to_it}")
        # print(station_to_delete.connections)
        time = station_to_delete.connections[station_next_to_it]
        self.current_station = self.stations_in_traject[index_new]
        # del self.stations_in_traject_name_only[self.station_counter - 1]

        time: int = int(time)
        self.time -= time
        
        
        # print("station deleted")

    def __repr__(self):
        return f"{self.name}, {self.stations_in_traject_name_only}\n"

  
