import sys
import random

sys.path.append('../')
from helpers import read_csv_file

sys.path.append('/classes')
from classes.stations import Station
from classes.traject import Traject
from classes.dienstregeling import Regeling
    
def run_breadth_first(self):
    self.aantal_trajecten = 3
    self.max_tijd_per_traject = 120
    specific_starts = {"Traject_1": "Dordrecht", "Traject_2": "Alkmaar"}
    self.visited_start_station = set()
    
    for i in range(self.aantal_trajecten):
        visited_stations = set()

        if f"Traject_{i+1}" in specific_starts:
        # Use the specific starting station
            random_station_name = specific_starts[f"Traject_{i+1}"]
            random_station = self.station_objects[random_station_name]
        else:
            while True:
                random_station_name = random.choice(list(self.station_objects.keys()))
                # print(f"Begin station: {random_station_name}")
                random_station = self.station_objects[random_station_name]
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
                        next_station = self.station_objects[next_station_name]
                        time_to_next_int = int(time_to_next)
                        # stack.append((next_station, current_time + time_to_next_int))

                        if current_time + time_to_next_int <= self.max_tijd_per_traject:
                            stack.append((next_station, current_time + time_to_next_int))
                        else:
                            time_remaining = False
                            break
                            
                        
                traject.add_station(current_station)
            print(traject)
            print(traject.time)
        self.traject_list.append(traject)
    
    for traject in self.traject_list:
        print(traject)

    score = calculate_score(self.traject_list)
    return score







