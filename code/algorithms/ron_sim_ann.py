import sys
sys.path.append('../')
from helpers import read_csv_file
import random
from ron_hill_climb import Algorithm, calculate_score, run_hill_climb_loop, run_alg_N_times

class SimulatedAnnealing(Algorithm):
    def __init__(self):
        self.T0 = 1
        self.T = 1

    def update_temperature(self):
        self.T = self.T - (self.T0 / self.iterations)
        
    def state_compare(self, new_state, state):
        if self.accept == True:
            state = new_state
            return state
        else:
            return state

    def accept(self, score_old, score_new):
        chance = 2 ^ (score_old - score_new) / self.T
        r = round(random.uniform(0, 1), 2)
        self.update_temperature

        if chance < r:
            return True
        else:
            return False

    def run_sim_ann(self):
        saved_states = []
        # geldige oplossing als input van het algoritme
        start_state = self.run_random_greedy()
        score_start_state = calculate_score(start_state)

        print(f"start state = {start_state}")
        print(f"Start score: {score_start_state}")
        
        saved_states.append(start_state)
        
        if len(saved_states) == 1:
            best_state = start_state
            score_best_state = calculate_score(best_state)

        self.iterations = 10

        for i in range(self.iterations):
            new_state, best_state = run_hill_climb_loop(best_state, self.max_tijd_per_traject, self.station_objects)
            score_state = calculate_score(new_state)
            score_best_state = calculate_score(best_state)
            state = self.state_compare(score_state, score_best_state, new_state, best_state)

        return state


    


    

