import sys
import random

sys.path.append('../')
from helpers import read_csv_file

sys.path.append('/classes')
from classes.stations import Station
from classes.traject import Traject
from classes.dienstregeling import Regeling
    
def run_breadth_first(algorithm_instance):
    aantal_trajecten = 3
    max_tijd_per_traject = 120
    specific_starts = {"Traject_1": "Dordrecht", "Traject_2": "Alkmaar"}
    visited_start_station = set()

    State = Regeling()
    
    for i in range(aantal_trajecten):
        visited_stations = set()

        if f"Traject_{i+1}" in specific_starts:
        # Use the specific starting station
            random_station_name = specific_starts[f"Traject_{i+1}"]
            random_station = algorithm_instance.station_objects[random_station_name]
        else:
            while True:
                random_station_name = random.choice(list(algorithm_instance.station_objects.keys()))
                # print(f"Begin station: {random_station_name}")
                random_station = algorithm_instance.station_objects[random_station_name]
                break

        stack = [(random_station, 0)]
        traject = Traject(f"Traject_{i+1}")
        time_remaining = True

        while stack and time_remaining:
            current_station, current_time = stack.pop(0)
            if current_station not in visited_stations:
                visited_stations.add(current_station)
                
                for next_station_name, time_to_next in current_station.connections.items():
                    if next_station_name not in visited_stations:
                        next_station = algorithm_instance.station_objects[next_station_name]
                        time_to_next_int = int(time_to_next)
                        # stack.append((next_station, current_time + time_to_next_int))

                        if current_time + time_to_next_int <= max_tijd_per_traject:
                            stack.append((next_station, current_time + time_to_next_int))
                        else:
                            time_remaining = False
                            break
                traject.add_station(current_station)

        # Update de toestand van de dienstregeling
        State.add_traject(traject)
    
    # Bereken de score van de gehele dienstregeling
    K = State.calculate_score(State.traject_list)

    return K







