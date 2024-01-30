import sys
import random
from typing import Set, Tuple, List, Dict

sys.path.append('../')
from helpers import read_csv_file

sys.path.append('/classes')
from classes.stations import Station
from classes.traject import Traject
from classes.dienstregeling import Regeling
from .depth_first import choose_start_station

"""
Implementatie van het Breadth First algoritme. Om dit algoritme aan te roepen
kan je dit script runnen.

Usage: 'python3 breadth_first.py holland' or 'python3 breadth_first.py nl' 
"""

# Maken van trajecten voor breadth_first algoritme
def compute_trajectory(algorithm_instance: Regeling, start_station: Station, all_visited_stations: Set[Station]) -> Traject:
    visited_stations: Set[Station] = set()
    stack: List[Tuple[Station, int]] = [(start_station, 0)]
    trajectory: Traject = Traject(f"Traject_{len(algorithm_instance.traject_list) + 1}")
    time_remaining = True

    while stack and time_remaining:
        current_station, current_time = stack.pop(0)
        if current_station not in visited_stations:
            visited_stations.add(current_station)
            all_visited_stations.add(current_station)
            trajectory.add_station(current_station)

            for next_station_name, time_to_next in current_station.connections.items():
                if next_station_name not in visited_stations:
                    next_station = algorithm_instance.station_objects[next_station_name]
                    time_to_next_int: int = int(time_to_next)
                    if current_time + time_to_next_int <= algorithm_instance.max_tijd_traject:
                        stack.append((next_station, current_time + time_to_next_int))
                    else:
                        time_remaining = False
                        break

    return trajectory


# Eenmalig runnen van het breadth_first algoritme
def run_breadth_first(algorithm_instance: Regeling) -> Tuple[Regeling, int]:
    visited_start_station: Set[Station] = set()
    used_connections: Set[Tuple[Station, Station]] = set() 
    all_visited_stations: Set[Station] = set()
    max_possible_connections = len(algorithm_instance.station_objects)

    # Initieer de states
    state: Regeling = Regeling(algorithm_instance.alle_connecties)

    # Loop over elk traject 
    while len(used_connections) < max_possible_connections:
        # Kies een start station
        start_station = choose_start_station(algorithm_instance, visited_start_station, len(all_visited_stations))
        visited_start_station.add(start_station)

        # Maak een traject
        trajectory = compute_trajectory(algorithm_instance, start_station, all_visited_stations)
        # Voeg traject toe aand dienstregeling
        state.add_traject(trajectory)
        if len(state.traject_list) == algorithm_instance.max_trajecten:
            break
    # Bet
    score: int = state.calculate_score()
    return state, score
