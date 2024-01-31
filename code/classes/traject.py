from .stations import Station

"""
Returnt een lijst met namen van stations die aan elkaar verbonden zijn.
Telt de totale duur van het traject op. 

Constraint: max 120 min per traject
"""
    

class Traject:

    def __init__(self, name, regio) -> None:
        self.name = name
        self.stations_in_traject = []
        self.stations_in_traject_name_only = []
        self.current_station = None
        self.station_counter = 0
        self.time = 0

        if regio == 'h':
            self.max_tijd = 120
        if regio == 'nl':
            self.max_tijd = 180
        
    
    def add_station(self, new_station: Station) -> None:

        # Voeg een station toe als de lijst nog leeg is
        if self.station_counter == 0:
            self.stations_in_traject.append(new_station)
            self.stations_in_traject_name_only.append(new_station.get_name())
            self.current_station = new_station
            self.station_counter += 1

        # Check voor een verbinding indien de lijst niet leeg is
        else:
            for connected_station_name, time in new_station.connections.items():
                if connected_station_name == self.current_station.get_name():
                    
                    # Station toevoegen aan traject lijst
                    self.stations_in_traject.append(new_station)    
                    self.stations_in_traject_name_only.append(new_station.get_name())
                    
                    # Nieuw station wordt huidig station
                    self.current_station = new_station  
                    time: int = int(time)

                    # Tel de tijd van het traject bij de totale tijd op
                    self.time += time   

                    # Aantal stations +1
                    self.station_counter += 1   

                    
    def delete_station(self) -> None:

        # Delete het laatste station van de lijst met objecten en namen
        station_to_delete = self.stations_in_traject.pop()
        self.stations_in_traject_name_only.pop()

        # Check de index van station achteraan in de lijst
        self.station_counter = len(self.stations_in_traject)
        index_new = self.station_counter - 1

        # Verander het huidige station naar laatste station in de lijst na deleten
        last_station_in_list_name = self.stations_in_traject[index_new].name
        time = station_to_delete.connections[last_station_in_list_name]
        self.current_station = self.stations_in_traject[index_new]

        # Trek tijd van verloren connectie af van totale tijd
        time: int = int(time)
        self.time -= time

    # Object representatie
    def __repr__(self):
        return f"{self.name}, {self.stations_in_traject_name_only}\n"
