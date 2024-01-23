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
    for traject in traject_list:
        #
        stations = traject.stations_in_traject
        for i in range(len(stations) - 1):
            connection = frozenset([stations[i].get_name(), stations[i+1].get_name()])
            unieke_connections.add(connection)

    print(f"unieke connecties: {len(unieke_connections)}")
    p = len(unieke_connections) / 28
    print(p)
    T = len(traject_list)
    print(T)
    Min = sum(traject.time for traject in traject_list)
    print(Min)
    # Bereken de score
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

    def run_random(self):
        self.aantal_trajecten = random.randint(1, 7)
        print(f"aantal trajecten: {self.aantal_trajecten}")
        

        for i in range(self.aantal_trajecten):
            self.max_tijd_per_traject = random.randint(1, 120)
            print(f"Max tijd voor traject {i}: {self.max_tijd_per_traject}")

            # random start station
            random_station_name = random.choice(list(self.station_objects.keys()))
            print(f"Begin station: {random_station_name}")
            random_station = self.station_objects[random_station_name]
        
            # begin een traject
            traject = Traject(f"Traject_{i+1}")
            
            # begin met het maken van een traject
            traject.add_station(random_station)
            
            # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
            connected_stations = list(random_station.connections.keys())
            print(f"stations met connectie aan beginstation: {connected_stations}")
            
             
            next_station_name = random.choice(connected_stations)
            next_station = self.station_objects[next_station_name]
            traject.add_station(next_station)
            random_station = next_station
            print(f"Traject na 1 verbinding: {traject}")
            print(f"Traject tijd na 1 verbinding: {traject.time}")
            
            # blijf stations toevoegen totdat de maximale tijd is bereikt
            while traject.time < self.max_tijd_per_traject:

                connected_stations = list(random_station.connections.keys())
                print(f"stations met connectie aan huidig: {connected_stations}")
 
                if not connected_stations:
                    break

                # Voeg random station toe aan traject
                next_station_name = random.choice(connected_stations)
                next_station = self.station_objects[next_station_name]

                # Check de tijd voordat je weer een station toevoegt 
                additional_time = int(random_station.connections[next_station_name])
                if traject.time + additional_time > self.max_tijd_per_traject:
                    break
                
                # voeg station toe
                print(f"Huidig traject voor toevoegen station: {traject}")
                traject.add_station(next_station)
                random_station = next_station
                print(f"Station dat zojuist is toegevoegd:{next_station_name}")
                print(f"tijd van de connectie: {additional_time}")

                print(f"Huidig traject na toevoegen station: {traject}")
                print(f"Totale Trajecttijd na toevoegen station: {traject.time}")

                

                # print(f"Traject_{i+1} na loop: {traject}")
                # print(f"Trajecttijd na loop voor Traject_{i+1}: {traject.time}")
                
            # Add the constructed traject to the list of trajects
            self.traject_list.append(traject)

            
            # print(f"Lijst met trajecten: {self.traject_list}")
        return self.traject_list
    
    def run_greedy(self):
        self.aantal_trajecten = 7
        self.max_tijd_per_traject = 120
        unieke_stations = set()

        for i in range(self.aantal_trajecten):
            random_station_name = random.choice(list(self.station_objects.keys()))
            print(f"Begin station: {random_station_name}")
            random_station = self.station_objects[random_station_name]

            # begin een traject
            traject = Traject(f"Traject_{i+1}")
            
            # begin met het maken van een traject
            traject.add_station(random_station)
            
            # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
            connected_stations = list(random_station.connections.keys())
            print(f"stations met connectie aan beginstation: {connected_stations}")
            
            if traject.station_counter == 1:
                current_station = random_station
                print(f"current_station: {current_station.get_name()}")

            unieke_stations.add(current_station)
            
            while traject.time < self.max_tijd_per_traject:
                next_station, time_to_next = self.find_best_connection(current_station, unieke_stations)


                # Check de tijd voordat je weer een station toevoegt 
                additional_time = int(random_station.connections[next_station_name])
                if traject.time + additional_time > self.max_tijd_per_traject:
                    break

            # next_station_name = random.choice(connected_stations)
        #     next_station = self.station_objects[next_station_name]
        #     traject.add_station(next_station)
        #     random_station = next_station

    def find_best_connection(new_station, unieke_stations):
        best_time = float('inf')
        best_station = None

        for connected_station, time in new_station.connections.items():
            if connected_station not in unieke_stations and time < best_time:
                best_time = time
                best_station = connected_station

        return best_station, best_time



randomm = Algorithm()
randomm.create_station_objects()
# traject_list = randomm.run_random()
traject_list = randomm.run_greedy()

# print(calculate_score(traject_list))



