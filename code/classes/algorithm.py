import sys
sys.path.append('../')

import time

from .stations import Station

from algorithms.randalg import run_randalg, run_randalg_bizzey, run_randalg_rustaaahg
from algorithms.greedy import run_greedy
from algorithms.hill_climber import run_hill_climber
from algorithms.depth_first import run_depth_first
from algorithms.breadth_first import run_breadth_first
from algorithms.simulated_annealing import run_simulated_annealing

class Algorithm:

    def __init__(self, name, stations_data, connections_data, max_trajecten, max_tijd_traject, alle_connecties):
        self.name = name
        self.station_objects = {}
        self.stations_data = stations_data
        self.connections_data = connections_data
        self.max_trajecten: int = max_trajecten
        self.max_tijd_traject: int = max_tijd_traject
        self.alle_connecties = alle_connecties

    # Voeg station objecten toe aan een lijst
    def create_station_objects(self):
        for row in self.stations_data:
            station_name = row[0]
            self.station_objects[station_name] = Station(station_name)

        # Voeg een tweede station toe om er zeker van te zijn dat er altijd 1 verbinding is
        for row in self.connections_data:
            main_station_name = row[0]
            connected_station_name = row[1]
            time = row[2]
            self.station_objects[main_station_name].create_connection(connected_station_name, time)
            self.station_objects[connected_station_name].create_connection(main_station_name, time)

        return self.station_objects
    
    # run_algorithm roept vershillende agoritmes in hun eigen script aan op verzoek van de gebruiker
    def run_algorithm(self, algorithm_instance, regio):
        self.algorithm_instance = algorithm_instance
        self.regio = regio

        if self.name == 'random':
            return run_randalg(algorithm_instance, regio)
            
        elif self.name == 'greedy':
            return run_greedy(algorithm_instance, regio)

        elif self.name == 'hill climber':
            return run_hill_climber(algorithm_instance, regio)

        elif self.name == 'depth first':
            return run_depth_first(algorithm_instance, regio)

        elif self.name == 'breadth first':
            return run_breadth_first(algorithm_instance, regio)
        
        elif self.name == 'simmulated annealing':
            return run_simulated_annealing(algorithm_instance, regio)
        
        elif self.name == 'bizzey':
            return run_randalg_bizzey(algorithm_instance)
            
        elif self.name == 'rustaaahg':
            return run_randalg_rustaaahg(algorithm_instance)
        
        else:
            raise AssertionError ("Geen valide naam!")
    

    def run_algorithm_for_60_sec(self, algorithm_instance):
        start = time.time()
        n_runs = 0
        scores_list = []
        self.algorithm_instance = algorithm_instance
        while time.time() - start < 60:
            print(f"run: {n_runs}")
            score = self.run_algorithm(self.algorithm_instance)
            n_runs += 1
            scores_list.append(score)
        return scores_list

    def run_algorithm_N_times(self, N, algorithm_instance, regio):
        scores_list = []
        self.algorithm_instance = algorithm_instance
        high_score = 0
        best_state = None

        for _ in range(N):
            results = self.run_algorithm(self.algorithm_instance, regio)
            state: object = results[0]
            score: int = results[1]
            scores_list.append(score)
            high_score = max(scores_list)

            for _ in results:
                if state.calculate_score() > high_score:
                    best_state = state

        return best_state, scores_list