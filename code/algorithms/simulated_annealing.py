import sys
sys.path.append('../')
from greedy import run_greedy
import random
import copy

sys.path.append('../')
from helpers import read_csv_file
from hill_climber import run_hill_climber, run_hill_climb_loop

sys.path.append('/classes')
from classes.stations import Station
from classes.traject import Traject
from classes.dienstregeling import Regeling


def run_simulated_annealing(algorithm_instance: Regeling):
    sim_ann = SimulatedAnnealing(algorithm_instance)
    State, K = sim_ann.run_sim_ann()
    return State, K


class SimulatedAnnealing:
    def __init__(self, algorithm_instance):
        self.algorithm_instance = algorithm_instance
        self.T0 = 80
        self.T = 120
        self.iterations = 170

    def update_temperature(self):
        self.T = float(self.T - (self.T0 / self.iterations))
        
    def state_compare(self, new_state, state):
        score_old = state.calculate_score()
        score_new = new_state.calculate_score()
        if self.accept(score_old, score_new):
            state = new_state
            return state
        else:
            return state

    def accept(self, score_old, score_new):
        # print(f"score_old - score_new: {score_old - score_new}")
        chance = 2 ** ((score_old - score_new) / self.T)
        # print(f"chance: {chance}")
        r = round(random.uniform(0, 1), 2)
        # print(f"r: {r}")
        self.update_temperature()

        if chance < r:
            # print("accept")
            return True
        else:
            # print("not accept")
            return False
 
    def run_sim_ann(self):
        # geldige oplossing als input van het algoritme
        start_state, K_start = run_greedy(self.algorithm_instance)
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
