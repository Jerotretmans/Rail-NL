import csv
from traject import Traject


class Regeling:
    """
    Een verzameling trajecten die samen zo veel mogelijk stations bereikt in zo min 
    mogelijk tijd, en waar elke verbinding gereden wordt. Score: K = p*10000 - (T*100 + Min)

    Constraint: max 7 trajecten in regio Holland, max 20 op nationaal niveau
    """
    def _init_(self) -> None:
        self.traject_list = []
        self.traject = Traject('Name')

    # Voeg een traject toe aan de lijst
    def add_traject(self, new_traject) -> None:
        assert len(self.traject_list) < 8, "Maximaal aantal trajecten berekit!"
        self.traject_list.append(new_traject)

    # Berekent de kwaliteitsscore van de gehele dienstregeling
    def calculate_score(self, traject_list):
        unique_connections = set()
        traject_counter = 0
        minutes = 0

        # Houd de variabelen bij
        for traject in self.traject_list:
            traject_counter += 1
            minutes += traject.time
            stations = traject.stations_in_traject

            for i in range(len(stations) - 1):
                connection = frozenset([stations[i].get_name(), stations[i+1].get_name()])
                unique_connections.add(connection)

        # Stel variabelen in
        p = len(unique_connections) / 28
        T = traject_counter
        Min = minutes

        # Bereken de score
        K = round(p * 10000 - (T * 100 + Min))     
        return K
    
    def export_output(self):
        csv_file_path = '../../output.csv'  
        
        with open(csv_file_path, 'w', newline='') as csvfile:
            # Create a CSV writer
            csv_writer = csv.writer(csvfile)

            # Write the header
            csv_writer.writerow(["train", "stations"])
            csv_writer.writerow(self.trajecten_in_regeling)
            csv_writer.writerow(["score",  self.calculate_score()])
        
        print(f"Output has been exported to {csv_file_path}")



# if __name__ == "__main__":
#     """
#     Test functie voordat we in main.py bezig gaan.
#     """

#     # Lees verbindingen van CSV bestand
#     connections = read_csv_file('../../data/ConnectiesHolland.csv')
    
#     test_stations = []
#     station1 = Station('Hoorn')
#     station2 = Station('Alkmaar')
#     station3 = Station('Den Helder')
#     station4 = Station('Gouda')
#     station5 = Station('Alkmaar')

#     test_stations.append(station1)
#     test_stations.append(station2)
#     test_stations.append(station3)
#     test_stations.append(station4)
#     test_stations.append(station5)

#     for row in connections:
#         main_station = row[0]
#         connected_station = row[1]
#         time = row[2]

#         for station in test_stations:
#             if station.name == main_station:
#                 station.create_connection(connected_station, time)
#             elif station.name == connected_station:
#                 station.create_connection(main_station, time)
    
#     name = "Train_1"
#     traject1 = Traject(name)
    
#     for station in test_stations:
#         print(f"Name: {station.get_name()}")
#         traject1.add_station(station)

#     regeling1 = Regeling("Regeling_1")
#     regeling1.add_traject(traject1)
#     # print(regeling1.calculate_T())
#     regeling1.export_output()
#     # print(regeling1.calculate_score())


    
    
