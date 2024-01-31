import sys
sys.path.append('../')
sys.path.append('/classes')

import random
import copy

from .greedy import run_greedy

from classes.dienstregeling import Regeling


def run_hill_climber(algorithm_instance, regio, aantal_trajecten) -> int:
    # Creeër een begin state middels het greedy algoritme
    start_state, K_start = run_greedy(algorithm_instance, regio, aantal_trajecten)
    # Begin state toewijzen als beste state
    best_state = start_state

    # Zet het aantal iteraties
    iterations = 100
    for _ in range(iterations):

        # Run de loop om een nieuwe state te verkrijgen
        state = run_hill_climb_loop(copy.deepcopy(best_state), algorithm_instance.station_objects)
        
        # Check of nieuwe state een verbetering is
        best_state = state_compare(state, best_state)

    # Bereken de score van de beste dienstregeling
    K = best_state.calculate_score()
    return best_state, K

"""
Runt hill climber iteratie met oude staat als input, en nieuwe staat als output.
"""
def run_hill_climb_loop(state, station_objects):
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
        
"""
Functie die oude staat vergelijkt met nieuwe state.
Wanneer nieuwe state beter is dan oude state, return nieuwe state
Wanneer oude staat beter is dan nieuwe staat, return oude state
"""
def state_compare(new_state, best_state):
    # bereken de score van die nieuw gegenereerde state en de oude state
    score_new_state = new_state.calculate_score()
    score_best_state = best_state.calculate_score()

    # Vergelijk de oude beste score met de score van de nieuwe state
    if score_new_state >= score_best_state:
        # Wanneer nieuwe state beter is dan oude beste state, wordt nieuwe state geaccepteerd als beste state
        best_state = copy.deepcopy(new_state)

    # print(f"best_state is nu: {best_state} met score: {score_best_state}")
    return best_state