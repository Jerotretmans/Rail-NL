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
def choose_start_station(algorithm_instance: Regeling, visited_start_station: Set[Station], index: int) -> Station:
    # Mogelijke specifieke start stations
    specific_starts: Dict[str, str] = {"Traject_1": "Dordrecht", "Traject_2": "Den Helder"}
    # gebruik start stations indien aanwezig
    if f"Traject_{index + 1}" in specific_starts:
        return algorithm_instance.station_objects[specific_starts[f"Traject_{index + 1}"]]
    # anders random station om te beginnen
    else:
        while True:
            random_station = random.choice(list(algorithm_instance.station_objects.values()))
            if random_station not in visited_start_station:
                return random_station
            
def can_lead_to_unvisited(station: Station, visited_stations, algorithm_instance: Regeling) -> bool:
    pass


# Functie voor het maken van trajecten
def compute_trajectory(algorithm_instance: Regeling, start_station: Station, all_visited_stations: Set[Station]) -> Traject:
    visited_stations: Set[Station] = set()
    stack: List[Tuple[Station, int]] = [(start_station, 0)]
    trajectory: Traject = Traject(f"Traject_{len(algorithm_instance.traject_list) + 1}")
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

def run_depth_first(algorithm_instance: Regeling) -> Tuple[Regeling, int]:
    visited_start_station: Set[Station] = set()
    all_possible_connections: Set[Tuple[Station, Station]] = set()
    used_connections: Set[Tuple[Station, Station]] = set()

    # Create a set of all possible connections between stations
    for station1 in algorithm_instance.station_objects.values():
        for station2, _ in station1.connections.items():
            all_possible_connections.add((station1, algorithm_instance.station_objects[station2]))

    # Initiate een state
    state: Regeling = Regeling(algorithm_instance.alle_connecties)

    # Continue generating trajectories until all exact connections are made
    while used_connections != all_possible_connections:
        # Choose a start station
        start_station = choose_start_station(algorithm_instance, visited_start_station, len(state.traject_list))
        # Voeg toe aan al gebruikte start stations
        visited_start_station.add(start_station)

        # Make a trajectory
        trajectory = compute_trajectory(algorithm_instance, start_station, used_connections)
        # Add the trajectory to the timetable
        state.add_traject(trajectory)
        print(trajectory)
        if len(state.traject_list) >= algorithm_instance.max_trajecten:
            break

    # Calculate the total score
    score: int = state.calculate_score()
    return state, score


# Eenmalige run van het Depth First algoritme
# def run_depth_first(algorithm_instance: Regeling) -> Tuple[Regeling, int]:
#     visited_start_station: Set[Station] = set()
#     used_connections: Set[Tuple[Station, Station]] = set() 
#     all_visited_stations: Set[Station] = set()
#     max_possible_connections = len(algorithm_instance.station_objects)
#     # Initieer de states
#     state: Regeling = Regeling(algorithm_instance.alle_connecties)

#     # Loop over elk traject 
#     while len(used_connections) < max_possible_connections:
#         # Kies een start station
#         start_station = choose_start_station(algorithm_instance, visited_start_station, len(state.traject_list))
#         visited_start_station.add(start_station)

#         # Maak een traject
#         trajectory = compute_trajectory(algorithm_instance, start_station, all_visited_stations)
#         # Voeg traject toe aand dienstregeling
#         state.add_traject(trajectory)
#         if len(state.traject_list) >= algorithm_instance.max_trajecten:
#             break

#     # Bereken de volledige score
#     score: int = state.calculate_score()
#     return state, score