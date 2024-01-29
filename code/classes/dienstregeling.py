import csv
from classes.traject import Traject


class Regeling:
    """
    Een verzameling trajecten die samen zo veel mogelijk stations bereikt in zo min 
    mogelijk tijd, en waar elke verbinding gereden wordt. Score: K = p*10000 - (T*100 + Min)

    Constraint: max 7 trajecten in regio Holland, max 20 op nationaal niveau
    """
    def __init__(self) -> None:
        self.traject_list = []
        self.traject = Traject('Name')

    # Voeg een traject toe aan de lijst
    def add_traject(self, new_traject) -> None:
        assert len(self.traject_list) < 8, "Maximaal aantal trajecten berekit!"
        self.traject_list.append(new_traject)

    # Berekent de kwaliteitsscore van de gehele dienstregeling
    def calculate_score(self):
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


    # Schrijft een csv bestand van een state
    def export_output():
        csv_file_path = 'data/output.csv'  

        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Header
            csv_writer.writerow(["train", "stations"])
            csv_writer.writerow(["trajecten in regeling"])
            csv_writer.writerow(["score"])

        print(f"Output has been exported to {csv_file_path}")