import sys
sys.path.append('../')
sys.path.append('/classes')

import random
import copy

from .greedy import run_greedy
from .hill_climber import run_hill_climb_loop

# Run het simulated annealing algoritme
def run_simulated_annealing(algorithm_instance, regio):
    sim_ann = SimulatedAnnealing(algorithm_instance)
    State, K = sim_ann.run_sim_ann()
    return State, K


class SimulatedAnnealing:
    """
    Simulated Annealing heeft zijn eigen class om het runnen van de functie
    wat overzichtelijker te maken.
    """

    # Initialiseer het algoritme, tempratuur, start tempratuur en iteraties
    def __init__(self, algorithm_instance):
        self.algorithm_instance = algorithm_instance
        self.T0 = 80
        self.T = 120
        self.iterations = 170

    # Update de temperatuur
    def update_temperature(self):
        self.T = float(self.T - (self.T0 / self.iterations))
    
    # Checkt of de nieuwe state is geaccepteerd door de accept functie en return de geaccepteerde state
    def state_compare(self, new_state, state):
        score_old = state.calculate_score()
        score_new = new_state.calculate_score()

        if self.accept(score_old, score_new):
            state = new_state
            return state
        else:
            return state
        
    # Bepaalt of een state wordt geaccepteerd
    def accept(self, score_old, score_new):
        chance = 2 ** ((score_old - score_new) / self.T)
        # Genereer een random float tussen 0 en 1
        r = round(random.uniform(0, 1), 2)
        # Update de tempraturr middels de functie
        self.update_temperature()

        # Wanneer de berekende chance kleiner is dat
        if chance < r:
            return True
        else:
            return False
 
    def run_sim_ann(self):
        # geldige oplossing als input van het algoritme
        start_state, K_start = run_greedy(self.algorithm_instance, 'h')
        best_state = copy.deepcopy(start_state)
        # print(f"score for best_state: {best_state.calculate_score()}")
        
        for i in range(self.iterations):
            new_state = run_sim_ann_loop(copy.deepcopy(best_state), self.algorithm_instance.station_objects)
            # print(f"score for current best_state: {best_state.calculate_score()}")
            # print(f"score for new state: {new_state.calculate_score()}")
            # breakpoint()
            best_state = self.state_compare(new_state, best_state)
        K = best_state.calculate_score()
        return best_state, K
    
def run_sim_ann_loop(state, station_objects):
    state = copy.deepcopy(state)
    # Loop over elk traject van de dienstregeling
    for traject in state.traject_list:

        # Delete een random hoeveelheid stations van het traject
        cut = random.randint(1, traject.station_counter)
        number_of_deletions = traject.station_counter - cut
        for i in range(number_of_deletions):
            traject.delete_station()

        # Voeg random stations toe zo lang ze niet boven maximale trajecttijd vallen
        while traject.time < traject.max_tijd:
            # Vind connecties aan het huidige station
            connected_stations = list(traject.current_station.connections.keys())
            connected_stations_not_in_traject = []

            # Maak een lijst van stations die nog niet in het traject zitten
            for station in connected_stations:
                if station not in traject.stations_in_traject_name_only:
                    connected_stations_not_in_traject.append(station)

            # Wanneer er geen stations meer kunnen worden toegevoegd wordt loop geeindigd.
            if len(connected_stations_not_in_traject) == 0:
                break
                    
            # Zoek een random station met connectie aan huidig station dat nog niet in het traject staat
            next_station_name = random.choice(connected_stations_not_in_traject)
            next_station = station_objects[next_station_name]

            # Check of totale trajecttijd niet wordt overschreden
            additional_time = int(traject.current_station.connections[next_station_name])
            if traject.time + additional_time > traject.max_tijd:
                break
            # Wanneer aan alle eisen is voldaan, kan station worden toegevoegd
            traject.add_station(next_station)

    # return de nieuwe state
    return state