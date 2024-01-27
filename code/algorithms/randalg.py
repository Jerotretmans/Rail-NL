import sys
sys.path.append('../')
sys.path.append('../classes')

from helpers import read_csv_file
import random

from stations import Station
from traject import Traject
from dienstregeling import Regeling

"""
Implementatie van het random algoritme. Om dit algoritme aan te roepen
kan je dit script runnen.

Usage: 'python3 randalg.py holland' or 'python3 randalg.py nl' 
"""

# Eenmalige run van het random algoritme
def run_randalg():

    # Roep een toestand op waarin de dienstregeling zich verkeert
    State = Regeling()

    # Random aantal trajecten
    aantal_trajecten = random.randint(1, 7)

    # Maximale tijd per traject
    max_tijd_per_traject = random.randint(1, 120)

    for i in range(aantal_trajecten):
        # random start station
        random_station_name = random.choice(list(station_objects.keys()))
        random_station = station_objects[random_station_name]
        
        # begin een traject
        traject = Traject(f"Traject_{i+1}")
        
        # begin met het maken van een traject
        traject.add_station(random_station)
        
        # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
        connected_stations = list(random_station.connections.keys())
        if connected_stations:  # Ensure there is at least one connected station
            next_station_name = random.choice(connected_stations)
            next_station = station_objects[next_station_name]
            traject.add_station(next_station)
            random_station = next_station
        
        # blijf stations toevoegen totdat de maximale tijd is bereikt
        while traject.time < max_tijd_per_traject:
            connected_stations = list(random_station.connections.keys())
            if not connected_stations:
                break
            
            # Voeg random station aan traject
            next_station_name = random.choice(connected_stations)
            next_station = station_objects[next_station_name]
            
            # Check de tijd voordat je weer een station toevoegt 
            additional_time = int(random_station.connections[next_station_name])
            if traject.time + additional_time > max_tijd_per_traject:
                break
            
            # voeg station toe
            traject.add_station(next_station)
            random_station = next_station
        
        # Update de toestand van de dienstregeling
        State.add_traject(traject)

    # Bereken de score van de gehele dienstregeling
    K = State.calculate_score(State.traject_list)

    return K
        
run_randalg()
N = 10000

def run_randalg_N_times(N):
    hist_list = []
    for i in range(N):
        score = run_randalg()
        hist_list.append(score)

    return hist_list

score_list = (run_randalg_N_times(N))

highest_score  = max(score_list)

print(f"Highest score: {highest_score}")


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

