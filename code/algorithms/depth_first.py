import sys
sys.path.append('../')
from helpers import read_csv_file, calculate_score
import random

sys.path.append('../classes')
from stations import Station
from traject import Traject
from dienstregeling import Regeling

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

    def run_depth_first(self):
    # bepaal max aantal trajecten en max tijd
        self.aantal_trajecten = 5
        self.max_tijd_per_traject = 120
        specific_starts = {"Traject_1": "Gouda", "Traject_2": "Dordrecht"}
        self.visited_start_station = set()
        self.all_visited_stations = set()
        
        # Maak elk traject
        for i in range(self.aantal_trajecten):
            # Maak een lege set om alle bezocte stations te onthouden
            visited_stations = set()

            if f"Traject_{i+1}" in specific_starts:
            # Use the specific starting station
                random_station_name = specific_starts[f"Traject_{i+1}"]
                random_station = self.station_objects[random_station_name]
            else:
            # Kies een random station om te beginnen
                while True:
                    random_station_name = random.choice(list(self.station_objects.keys()))
                    random_station = self.station_objects[random_station_name]
                    if random_station not in self.visited_start_station:
                        self.visited_start_station.add(random_station)
                        break
                # Start de stack met het eerste station en de tijd op 0
            stack = [(random_station, 0)]
                # Maak een traject aan om het nieuwe traject op te slaan
            traject = Traject(f"Traject_{i+1}")
                # Boolean om bij te houden of de maximale tijd niet wordt overschreden
            time_remaining = True

                # Loop totdat de stack op is of de maximale tijd is bereikt
            while stack and time_remaining:
                    # Pop een station van de stack
                current_station, current_time = stack.pop()
                    # check of een station al bezicht is
                if current_station not in visited_stations:
                        # Voeg hem toe aan bezochte stations in traject
                    visited_stations.add(current_station)
                        # Voeg toe aan al de bezochte stations
                    self.all_visited_stations.add(current_station) 
                        # Voeg het station toe aan het traject
                    traject.add_station(current_station)
                        
                        # Ga over de verbonden stations
                    for next_station_name, time_to_next in current_station.connections.items():
                            # Kijk of een verbonden station al bezocht is en zo niet dan...
                        if next_station_name not in visited_stations and next_station_name:
                            next_station = self.station_objects[next_station_name]
                            time_to_next_int = int(time_to_next)

                                # Check of het toevoegen van die connectie niet de maximale tijd overschrijdt 
                            if current_time + time_to_next_int <= self.max_tijd_per_traject:
                                stack.append((next_station, current_time + time_to_next_int))
                                # als het toevoegen de tijd zou overschrijden break dan uit de loop en de while loop
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

        score = algorithm.run_depth_first()

        hist_list.append(score)

    return hist_list

score_list = (run_alg_N_times(N))
# print(score_list)
highest_score  = max(score_list)

print(f"Highest score: {highest_score}")





