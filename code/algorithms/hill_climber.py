import sys
sys.path.append('../')
sys.path.append('/classes')

import random
import copy

from .greedy import run_greedy

from classes.dienstregeling import Regeling


def run_hill_climber(algorithm_instance: Regeling, regio) -> int:
    # State = Regeling(algorithm_instance.alle_connecties)

    start_state, K_start = run_greedy(algorithm_instance, regio)

    best_state, K_best = start_state, K_start
    iterations = 100
    for _ in range(iterations):
        state = run_hill_climb_loop(best_state, algorithm_instance.max_tijd_traject, algorithm_instance.station_objects)
        K = state.calculate_score()
        best_state = state_compare(K, K_best, state, best_state)
    

    # Bereken de score van de gehele dienstregeling
    K: int = best_state.calculate_score()
    return best_state, K

def run_hill_climb_loop(state, max_time, station_objects):
    for traject in state.traject_list:
        # print("Oude trajecten:")
        # print(traject)
        # print(f"Aantal stations in traject: {traject.station_counter}")
        # print(traject.time)
        # print()
        # print(f"traject voor de cut: {traject}")
        traject_voor_deletions = copy.deepcopy(traject)
        cut = random.randint(1, traject.station_counter)
        index_current_station = cut - 1
        number_of_deletions = traject.station_counter - cut
        # print(f"number of deletetions: {number_of_deletions}")
        for i in range(number_of_deletions):
            traject.delete_station()
        # print(f"Traject na het cutten is: {traject}")
        # print(f"current station na cutten is: {traject.current_station.get_name()}")
        # print()

        while traject.time < max_time:
            connected_stations = list(traject.current_station.connections.keys())
            # print(f"Huidig traject is nu: {traject}")
            connected_stations_not_in_traject = []
            for station in connected_stations:
                if station not in traject.stations_in_traject_name_only:
                    connected_stations_not_in_traject.append(station)
            
            # print(traject.stations_in_traject_name_only)
            # print(f"stations met connectie aan huidig station en niet in traject: {connected_stations_not_in_traject}")

            if len(connected_stations_not_in_traject) == 0:
                break
                    
            # Voeg random station toe aan traject dat nog niet is gekozen
            next_station_name = random.choice(connected_stations_not_in_traject)
            # print(f"next station name = {next_station_name}")
            next_station = station_objects[next_station_name]

            # Check de tijd voordat je weer een station toevoegt 
            additional_time = int(traject.current_station.connections[next_station_name])
            if traject.time + additional_time > max_time:
                break
            traject.add_station(next_station)
            # print(f"Huidig traject is: {traject}")
            # print(f"Traject_time: {traject.time}")

    # for traject in copy_state.traject_list:
    #     print(traject)

    # for traject in state.traject_list:
    #     print(traject)
    return state
        

def state_compare(score_current_state, score_best_state, current_state, best_state):
    if score_current_state >= score_best_state:
        best_state = current_state
        score_best_state = best_state.calculate_score()
    # print(f"best_state is nu: {best_state} met score: {score_best_state}")
    return best_state