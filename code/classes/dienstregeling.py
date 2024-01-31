from classes.traject import Traject


"""
Een verzameling trajecten die samen zo veel mogelijk stations bereikt in zo min 
mogelijk tijd, en waar elke verbinding gereden wordt. Score: K = p*10000 - (T*100 + Min)

Constraint: max 7 trajecten in regio Holland, max 20 op nationaal niveau
"""

class Regeling:

    def __init__(self, regio) -> None:
        self.traject_list = []
        self.traject = Traject('Name', regio)

        if regio == 'h':
            self.max_trajecten = 7
            self.alle_connecties = 28
        elif regio == 'nl':
            self.max_trajecten = 20
            self.alle_connecties = 89

    # Voeg een traject toe aan de lijst
    def add_traject(self, new_traject) -> None:
        self.traject_list.append(new_traject)

    # Berekent de kwaliteitsscore van de gehele dienstregeling
    def calculate_score(self) -> int:
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
        p = len(unique_connections) / self.alle_connecties
        T = traject_counter
        Min = minutes

        # Bereken de score
        K = round(p * 10000 - (T * 100 + Min))
        return K

    # Object representatie
    def __repr__(self):
        return f"{self.traject}: {self.traject_list}"