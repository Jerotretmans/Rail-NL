from classes.traject import Traject
from classes.dienstregeling import Regeling
from .depth_first import choose_start_station

"""
Implementatie van het Breadth First algoritme.
"""

# Maken van trajecten voor breadth_first algoritme
def compute_trajectory(algorithm_instance, start_station, all_visited_stations, traject_counter, regio) -> Traject:
    visited_stations = set()
    stack = [(start_station, 0)]
    trajectory = Traject(f"Traject_{traject_counter}", regio)
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
def run_breadth_first(algorithm_instance, regio):
    visited_start_station = set()
    all_possible_connections = {(station1, algorithm_instance.station_objects[station2]) for station1 in algorithm_instance.station_objects.values() for station2 in station1.connections}
    used_connections = set()
    traject_counter = 1

    state = Regeling(regio)

    # Blijf trajecten maken totdat alle connecties zijn gereden
    while used_connections != all_possible_connections:

        start_station = choose_start_station(algorithm_instance, visited_start_station)
        visited_start_station.add(start_station)

        # Maak een Traject
        trajectory = compute_trajectory(algorithm_instance, start_station, used_connections, traject_counter, regio)
        traject_counter += 1
        state.add_traject(trajectory)
        
        # Zorg dat je niet te veel trajecten maakt
        if len(state.traject_list) == algorithm_instance.max_trajecten:
            break

    # Calculate the total score
    score = state.calculate_score()
    return state, score