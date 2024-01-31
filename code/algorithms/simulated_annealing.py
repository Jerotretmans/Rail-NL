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
            new_state = run_hill_climb_loop(copy.deepcopy(best_state), self.algorithm_instance.max_tijd_traject, self.algorithm_instance.station_objects)
            # print(f"score for current best_state: {best_state.calculate_score()}")
            # print(f"score for new state: {new_state.calculate_score()}")
            # breakpoint()
            best_state = self.state_compare(new_state, best_state)
        K = best_state.calculate_score()
        return best_state, K