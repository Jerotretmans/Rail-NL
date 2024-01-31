import sys
import random
from typing import Dict, Set, List, Tuple

sys.path.append('../')
from helpers import read_csv_file

sys.path.append('/classes')
from classes.stations import Station
from classes.traject import Traject
from classes.dienstregeling import Regeling

"""
Implementatie van het Depth First algoritme. Om dit algoritme aan te roepen
kan je dit script runnen.

Usage: 'python3 depth_first.py holland' or 'python3 depth_first.py nl' 
"""

# Functie voor kiezen van start stations voor trajecten
def choose_start_station(algorithm_instance: Regeling, visited_start_station: Set[Station]) -> Station:
    return random.choice([station for station in algorithm_instance.station_objects.values() if station not in visited_start_station])
            
def can_lead_to_unvisited(station: Station, visited_stations) -> bool:
    return any(neighbor_name not in visited_stations for neighbor_name in station.connections)

# Functie voor het maken van trajecten
def compute_trajectory(algorithm_instance: Regeling, start_station: Station, all_visited_stations: Set[Station], traject_counter) -> Traject:
    visited_stations: Set[Station] = set()
    stack: List[Tuple[Station, int]] = [(start_station, 0)]
    trajectory: Traject = Traject(f"Traject_{traject_counter}")
    time_remaining = True

    # Loop totdat de stack leeg is of de maximale tijd is bereikt
    while stack and time_remaining:
        current_station, current_time = stack.pop()
        # Check of station al bezocht is
        if current_station not in visited_stations:
            # Voeg toe aan bezochte stations
            visited_stations.add(current_station)
            all_visited_stations.add(current_station)
            # Voeg toe aan traject
            trajectory.add_station(current_station)

            # Sort connections based on the number of unvisited connections
            sorted_connections = sorted(current_station.connections.items(), 
                                        key=lambda item: sum(neighbor not in visited_stations for neighbor in algorithm_instance.station_objects[item[0]].connections),
                                        reverse=True)

            for next_station_name, time_to_next in sorted_connections:
                if next_station_name not in visited_stations:
                    next_station = algorithm_instance.station_objects[next_station_name]
                    time_to_next_int: int = int(time_to_next)
                    if current_time + time_to_next_int <= algorithm_instance.max_tijd_traject:
                        if next_station_name not in visited_stations or can_lead_to_unvisited(next_station, visited_stations, algorithm_instance):
                            stack.append((next_station, current_time + time_to_next_int))
                    else:
                        time_remaining = False
                        break
    return trajectory

def run_depth_first(algorithm_instance: Regeling) -> Tuple[Regeling, int]:
    visited_start_station: Set[Station] = set()
    all_possible_connections: Set[Tuple[Station, Station]] = set()
    used_connections: Set[Tuple[Station, Station]] = set()
    traject_counter = 1

    # Create a set of all possible connections between stations
    for station1 in algorithm_instance.station_objects.values():
        for station2, _ in station1.connections.items():
            all_possible_connections.add((station1, algorithm_instance.station_objects[station2]))
            
    state: Regeling = Regeling(algorithm_instance.alle_connecties)

    # Continue generating trajectories until all exact connections are made
    while used_connections != all_possible_connections:
        start_station = choose_start_station(algorithm_instance, visited_start_station)
        visited_start_station.add(start_station)

        # Make a trajectory
        trajectory = compute_trajectory(algorithm_instance, start_station, used_connections, traject_counter)
        traject_counter += 1
        state.add_traject(trajectory)
        print(trajectory)

        if len(state.traject_list) >= algorithm_instance.max_trajecten:
            break

    # Calculate the total score
    score: int = state.calculate_score()
    return state, score