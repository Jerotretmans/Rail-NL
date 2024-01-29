import sys
sys.path.append('../')
sys.path.append('/classes')

import random
from typing import Dict, List

from classes.traject import Traject
from classes.dienstregeling import Regeling
from classes.stations import Station


"""
Implementatie van het random algoritme. Om dit algoritme aan te roepen
kan je dit script runnen.

Usage: 'python3 randalg.py holland' or 'python3 randalg.py nl' 
"""

# Eenmalige run van het random algoritme
def run_randalg(algorithm_instance: Regeling) -> int:

    # Roep een toestand op waarin de dienstregeling zich verkeert
    State: Regeling = Regeling(algorithm_instance.alle_connecties)

    # Random aantal trajecten
    aantal_trajecten: int = random.randint(1, algorithm_instance.max_trajecten)

    # Maximale tijd per traject
    max_tijd_per_traject: int = random.randint(1, 120)

    for i in range(aantal_trajecten):
        # random start station
        random_station_name: str = random.choice(list(algorithm_instance.station_objects.keys()))
        random_station: Station = algorithm_instance.station_objects[random_station_name]
        
        # begin een traject
        traject: Traject = Traject(f"Traject_{i+1}")
        
        # begin met het maken van een traject
        traject.add_station(random_station)
        
        # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
        connected_stations: List[str] = list(random_station.connections.keys())
        if connected_stations:  # Ensure there is at least one connected station
            next_station_name: str = random.choice(connected_stations)
            next_station: Station = algorithm_instance.station_objects[next_station_name]
            traject.add_station(next_station)
            random_station = next_station
        
        # blijf stations toevoegen totdat de maximale tijd is bereikt
        while traject.time < max_tijd_per_traject:
            connected_stations = list(random_station.connections.keys())
            if not connected_stations:
                break
            
            # Voeg random station aan traject
            next_station_name: str = random.choice(connected_stations)
            next_station = algorithm_instance.station_objects[next_station_name]
            
            # Check de tijd voordat je weer een station toevoegt 
            additional_time: int = int(random_station.connections[next_station_name])
            if traject.time + additional_time > max_tijd_per_traject:
                break
            
            # voeg station toe
            traject.add_station(next_station)
            random_station = next_station
        
        # Update de toestand van de dienstregeling
        State.add_traject(traject)
    

    # Bereken de score van de gehele dienstregeling
    K: int = State.calculate_score()
    return State, K
