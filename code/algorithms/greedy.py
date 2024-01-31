import random
from typing import Dict, List

from classes.traject import Traject
from classes.dienstregeling import Regeling


"""
Implementatie van het greedy algoritme.
"""

# Eenmalige run van het random algoritme
def run_greedy(algorithm_instance, regio) -> int:

    # Roep een toestand op waarin de dienstregeling zich verkeert
    State = Regeling(regio)

    # Random aantal trajecten
    aantal_trajecten: int = algorithm_instance.max_trajecten
    
    for i in range(aantal_trajecten):
        # Maximale tijd per traject
        max_tijd_per_traject: int = random.randint(40, traject.max_tijd)

        # random start station
        random_station_name: str = random.choice(list(algorithm_instance.station_objects.keys()))
        random_station = algorithm_instance.station_objects[random_station_name]
        
        # begin een traject
        traject = Traject(f"Traject_{i+1}", regio)
        
        # begin met het maken van een traject
        traject.add_station(random_station)
        
        # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
        connected_stations = list(random_station.connections.keys())

        if traject.station_counter == 1:
            current_station = random_station

        while traject.time < traject.max_tijd:
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
    K: int = State.calculate_score()
    return State, K
