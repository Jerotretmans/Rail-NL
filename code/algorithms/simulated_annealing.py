import sys
sys.path.append('../')
sys.path.append('/classes')

import random
import copy

from .greedy import run_greedy
from .hill_climber import run_hill_climb_loop

from code.visualisation.plot import plot_scores

T0_options = []
T_options = []
iterations_options = []

for i in range(20, 220, 20):
    T0_options.append(i)
    T_options.append(i)
    iterations_options.append(i)


def run_simulated_annealing(algorithm_instance, regio):
    sim_ann = SimulatedAnnealing(algorithm_instance)
    State, K, sim_list = sim_ann.run_sim_ann()
    plot_scores(sim_list, sim_ann.iterations)
    return State, K


class SimulatedAnnealing:
    def __init__(self, algorithm_instance):
        self.algorithm_instance = algorithm_instance
        # for T0 in T0_options:
        #     self.T0 = T0
        # for T in T_options:
        #     self.T = T
        # for iterations in iterations_options:
        #     self.iterations = iterations
        self.T0 = 120
        self.T = 110
        self.iterations = 130
        self.sim_list = []

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
        start_state, K_start = run_greedy(self.algorithm_instance, 'h')
        best_state = copy.deepcopy(start_state)
        # print(f"score for best_state: {best_state.calculate_score()}")
        
        for _ in range(self.iterations):
            new_state = run_hill_climb_loop(copy.deepcopy(best_state), self.algorithm_instance.max_tijd_traject, self.algorithm_instance.station_objects)
            score = new_state.calculate_score()
            # print(f"score for current best_state: {best_state.calculate_score()}")
            # print(f"score for new state: {new_state.calculate_score()}")
            # breakpoint()
            best_state = self.state_compare(new_state, best_state)
            self.sim_list.append(score)

        K = best_state.calculate_score()
        return best_state, K, self.sim_list
