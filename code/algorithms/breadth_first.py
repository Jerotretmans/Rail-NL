import sys
sys.path.append('../')
from helpers import read_csv_file
import random

sys.path.append('../classes')
from stations import Station
from traject import Traject
from dienstregeling import Regeling

def calculate_score(traject_list):
    unieke_connections = set()
    traject_counter = 0
    Min = 0

    for traject in traject_list:
        traject_counter += 1
        # print(f"tijd per traject: {traject.time}")
        Min += traject.time
        # print(Min)
        stations = traject.stations_in_traject
        for i in range(len(stations) - 1):
            connection = frozenset([stations[i].get_name(), stations[i+1].get_name()])
            unieke_connections.add(connection)

    # print("Calculate score:")
    # print(f"unieke connecties: {len(unieke_connections)}")
    p = len(unieke_connections) / 28
    # print(f"p = {p}")
    T = traject_counter
    # print(f"T = {T}")
    Min = sum(traject.time for traject in traject_list)
    # print(f"Min = {Min}")
    # # Bereken de score
    K = round(p * 10000 - (T * 100 + Min))     
    return K

class Algorithm:
    def __init__(self):
        self.stations_data = read_csv_file('../../data/StationsHolland.csv')
        self.connections_data = read_csv_file('../../data/ConnectiesHolland.csv')
        self.station_objects = {}
        self.traject_list = []
    

    def create_station_objects(self):
        for row in self.stations_data:
            station_name = row[0]
            self.station_objects[station_name] = Station(station_name)
            
        for row in self.connections_data:
            main_station_name = row[0]
            connected_station_name = row[1]
            time = row[2]
            self.station_objects[main_station_name].create_connection(connected_station_name, time)
            self.station_objects[connected_station_name].create_connection(main_station_name, time)
        
        return self.station_objects

    
    def run_breadth_first(self):
        self.aantal_trajecten = 5
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


N = 1
def run_alg_N_times(N):
    hist_list = []
    for i in range(N):

        algorithm = Algorithm()
        algorithm.create_station_objects()

        score = algorithm.run_breadth_first()

        hist_list.append(score)

    return hist_list

score_list = (run_alg_N_times(N))
# print(score_list)
highest_score  = max(score_list)

print(f"Highest score: {highest_score}")





