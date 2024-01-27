import sys
sys.path.append('../')
from helpers import read_csv_file
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

    def run_random(self):
        self.aantal_trajecten = random.randint(1, 7)
        # print(f"aantal trajecten: {self.aantal_trajecten}")
        

        for i in range(self.aantal_trajecten):
            self.max_tijd_per_traject = random.randint(1, 120)
            # print(f"Max tijd voor traject {i}: {self.max_tijd_per_traject}")

            # random start station
            random_station_name = random.choice(list(self.station_objects.keys()))
            # print(f"Begin station: {random_station_name}")
            random_station = self.station_objects[random_station_name]
        
            # begin een traject
            traject = Traject(f"Traject_{i+1}")
            
            # begin met het maken van een traject
            traject.add_station(random_station)
            
            # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
            connected_stations = list(random_station.connections.keys())
            # print(f"stations met connectie aan beginstation: {connected_stations}")
            
             
            next_station_name = random.choice(connected_stations)
            next_station = self.station_objects[next_station_name]
            traject.add_station(next_station)
            random_station = next_station
            # print(f"Traject na 1 verbinding: {traject}")
            # print(f"Traject tijd na 1 verbinding: {traject.time}")
            
            # blijf stations toevoegen totdat de maximale tijd is bereikt
            while traject.time < self.max_tijd_per_traject:

                connected_stations = list(random_station.connections.keys())
                # print(f"stations met connectie aan huidig: {connected_stations}")
 
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
                # print(f"Huidig traject voor toevoegen station: {traject}")
                traject.add_station(next_station)
                random_station = next_station
                # print(f"Station dat zojuist is toegevoegd:{next_station_name}")
                # print(f"tijd van de connectie: {additional_time}")

                # print(f"Huidig traject na toevoegen station: {traject}")
                # print(f"Totale Trajecttijd na toevoegen station: {traject.time}")

                

                # print(f"Traject_{i+1} na loop: {traject}")
                # print(f"Trajecttijd na loop voor Traject_{i+1}: {traject.time}")
                
            # Add the constructed traject to the list of trajects
            self.traject_list.append(traject)

            
            # print(f"Lijst met trajecten: {self.traject_list}")
        return self.traject_list
        
    
    def run_random_greedy(self):
        self.aantal_trajecten = random.randint(4, 5)
        

        for i in range(self.aantal_trajecten):
            self.max_tijd_per_traject = random.randint(40, 120)
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
            
            while traject.time < self.max_tijd_per_traject:
                best_time = float('inf')
                best_station = None
     
                for connected_station_name, time in current_station.connections.items():
                    time = float(time)
                    if connected_station_name not in traject.get_names() and time < best_time:
                        best_time = time
                        best_station = connected_station_name

                # Check de tijd voordat je weer een station toevoegt 
                if traject.time + best_time > self.max_tijd_per_traject:
                    break

                next_station_name = best_station
                next_station = self.station_objects[next_station_name]
                traject.add_station(next_station)

                current_station = next_station


                print(traject)
                print(traject.time)
            self.traject_list.append(traject)
        
        return self.traject_list

    def run_hill_climber(self):
        saved_states = []
        # geldige oplossing als input van het algoritme
        start_state = self.run_random_greedy()
        score_start_state = calculate_score(start_state)
        # print(score_start_state)
        print(f"start state = {start_state}")
        print(f"Start score: {score_start_state}")
        saved_states.append(start_state)
        
        if len(saved_states) == 1:
            best_state = start_state
            score_best_state = calculate_score(best_state)
        
        state = run_hill_climb_loop(best_state, self.max_tijd_per_traject, self.station_objects, score_best_state)
        return state

def run_hill_climb_loop(state, max_time, station_objects, score_best_state):
    counter = 0
    best_state = state
    for traject in state:
            print("Oude trajecten:")
            print(traject)
            print(f"Aantal stations in traject: {traject.station_counter}")
            print(traject.time)
            print()

            cut = random.randint(1, traject.station_counter)
            number_of_deletions = traject.station_counter - cut
            print(f"number of deletetions: {number_of_deletions}")
            
            # del traject.stations_in_traject[cut:traject.station_counter]
            for i in range(0, number_of_deletions):
                traject.delete_station()
            
            print(f"Traject na het cutten is: {traject}")

            traject.current_station = traject.stations_in_traject[cut - 1]
            print(f"current station na cutten is: {traject.current_station.get_name()}")
            
            while traject.time < max_time:
                connected_stations = list(traject.current_station.connections.keys())
                print(f"Huidig traject is nu: {traject}")
                print(f"Huidige score is nu: {calculate_score(state)}")
                print(f"huidig station is nu: {traject.current_station.get_name()}")
                
                # print(f"stations in traject: {traject.stations_in_traject}")
                
                connected_stations_not_in_traject = []
                for station in connected_stations:
                    if station not in traject.stations_in_traject_name_only:
                        connected_stations_not_in_traject.append(station)

                print(traject.stations_in_traject_name_only)
                print(f"stations met connectie aan huidig station en niet in traject: {connected_stations_not_in_traject}")

                if len(connected_stations_not_in_traject) == 0:
                    break
                        
                # Voeg random station toe aan traject dat nog niet is gekozen
                next_station_name = random.choice(connected_stations_not_in_traject)
                print(f"next station name = {next_station_name}")
                next_station = station_objects[next_station_name]

                # Check de tijd voordat je weer een station toevoegt 
                additional_time = int(traject.current_station.connections[next_station_name])
                if traject.time + additional_time > max_time:
                    break

                traject.add_station(next_station)
                print("succes")

            score_state = calculate_score(state)
            
            # print("Nieuwe trajecten:")
            # print(traject)
            # print(f"Test: {score_state}")
            # print(f"Best: {score_best_state}")
            # print(f"Aantal stations in traject: {traject.station_counter}")
            # print(traject.time)
            # print()

            if score_state >= score_best_state:
                best_state = state
                score_best_state = score_state
            print(f"best_state is nu: {best_state} met score: {score_best_state}")

    return best_state



N = 100
def run_alg_N_times(N):
    hist_list = []
    for i in range(N):

        algorithm = Algorithm()
        algorithm.create_station_objects()

        # to run random alg N times
        # state = algorithm.run_random()
        # score = calculate_score(state)

        # to run greedy alg N times
        # state = algorithm.run_random_greedy()
        # score = calculate_score(state)

        # to run hill_climber N times
        state = algorithm.run_hill_climber()
        score = calculate_score(state)

        hist_list.append(score)

    return hist_list

score_list = (run_alg_N_times(N))
print(score_list)
highest_score  = max(score_list)

print(f"Highest score: {highest_score}")