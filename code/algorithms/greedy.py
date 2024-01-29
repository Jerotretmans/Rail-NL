import sys
import random
from typing import Dict, List

sys.path.append('../')
from helpers import read_csv_file
sys.path.append('/classes')
from classes.stations import Station
from classes.traject import Traject
from classes.dienstregeling import Regeling


"""
Implementatie van het random algoritme. Om dit algoritme aan te roepen
kan je dit script runnen.

Usage: 'python3 randalg.py holland' or 'python3 randalg.py nl' 
"""

# Eenmalige run van het random algoritme
def run_greedy(algorithm_instance: Regeling) -> int:
    # Roep een toestand op waarin de dienstregeling zich verkeert
    State = Regeling(algorithm_instance.alle_connecties)

    # Random aantal trajecten
    # aantal_trajecten: int = random.randint(4, 5)

    for i in range(algorithm_instance.max_trajecten):
        # Maximale tijd per traject
        max_tijd_per_traject: int = random.randint(40, algorithm_instance.max_tijd_traject)

        # random start station
        random_station_name: str = random.choice(list(algorithm_instance.station_objects.keys()))
        random_station: Station = algorithm_instance.station_objects[random_station_name]
        
        # begin een traject
        traject: Traject = Traject(f"Traject_{i+1}")
        
        # begin met het maken van een traject
        traject.add_station(random_station)
        
        # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
        connected_stations = list(random_station.connections.keys())

        if traject.station_counter == 1:
            current_station: Station = random_station

        while traject.time < algorithm_instance.max_tijd_traject:
            best_time: float = float('inf')
            best_station: str = None

            for connected_station_name, time in current_station.connections.items():
                time: float = float(time)
                if connected_station_name not in traject.stations_in_traject_name_only and time < best_time:
                    best_time = time
                    best_station = connected_station_name

            # Check de tijd voordat je weer een station toevoegt 
            if traject.time + best_time > max_tijd_per_traject:
                break

            next_station_name: str = best_station
            next_station = algorithm_instance.station_objects[next_station_name]
            traject.add_station(next_station)
            current_station = next_station
        
        # Update de toestand van de dienstregeling
        State.add_traject(traject)
    

    # Bereken de score van de gehele dienstregeling
    K: int = State.calculate_score(State.traject_list)
    return State, K
