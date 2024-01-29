import sys
import random
from typing import Dict, Set, List, Tuple

sys.path.append('../')
from helpers import read_csv_file

sys.path.append('/classes')
from classes.stations import Station
from classes.traject import Traject
from classes.dienstregeling import Regeling

"""
Implementatie van het Depth First algoritme. Om dit algoritme aan te roepen
kan je dit script runnen.

Usage: 'python3 depth_first.py holland' or 'python3 depth_first.py nl' 
"""


# Eenmalige run van het Depth First algoritme
def run_depth_first(algorithm_instance: Regeling) -> int:

    # bepaal max aantal trajecten en max tijd
    # max_tijd_per_traject: int = 120
    specific_starts: Dict[str, str] = {"Traject_1": "Gouda", "Traject_2": "Dordrecht"}
    visited_start_station: Set[Station] = set()
    all_visited_stations: Set[Station] = set()


    # Roep een toestand op waarin de dienstregeling zich verkeert
    State: Regeling = Regeling(algorithm_instance.alle_connecties)    
    
    # Maak elk traject
    for i in range(algorithm_instance.max_trajecten):
        # Maak een lege set om alle bezocte stations te onthouden
        visited_stations: Set[Station] = set()
        # Gebruik de aangegeven start stations indien die aangegeven zijn
        if f"Traject_{i+1}" in specific_starts:
            random_station_name: str = specific_starts[f"Traject_{i+1}"]
            random_station = algorithm_instance.station_objects[random_station_name]
        else:
        # Kies een random station om te beginnen
            while True:
                random_station_name: str = random.choice(list(algorithm_instance.station_objects.keys()))
                random_station = algorithm_instance.station_objects[random_station_name]
                if random_station not in visited_start_station:
                    visited_start_station.add(random_station)
                    break
            # Start de stack met het eerste station en de tijd op 0
        stack: List[Tuple[Station, int]] = [(random_station, 0)]
            # Maak een traject aan om het nieuwe traject op te slaan
        traject: Traject = Traject(f"Traject_{i+1}")
            # Boolean om bij te houden of de maximale tijd niet wordt overschreden
        time_remaining: bool = True
            # Loop totdat de stack op is of de maximale tijd is bereikt
        while stack and time_remaining:
                # Pop een station van de stack
            current_station, current_time = stack.pop()
                # check of een station al bezicht is
            if current_station not in visited_stations:
                    # Voeg hem toe aan bezochte stations in traject
                visited_stations.add(current_station)
                    # Voeg toe aan al de bezochte stations
                all_visited_stations.add(current_station) 
                    # Voeg het station toe aan het traject
                traject.add_station(current_station)
                    
                    # Ga over de verbonden stations
                for next_station_name, time_to_next in current_station.connections.items():
                        # Kijk of een verbonden station al bezocht is en zo niet dan...
                    if next_station_name not in visited_stations and next_station_name:
                        next_station = algorithm_instance.station_objects[next_station_name]
                        time_to_next_int: int = int(time_to_next)
                            # Check of het toevoegen van die connectie niet de maximale tijd overschrijdt 
                        if current_time + time_to_next_int <= algorithm_instance.max_tijd_traject:
                            stack.append((next_station, current_time + time_to_next_int))
                            # als het toevoegen de tijd zou overschrijden break dan uit de loop en de while loop
                        else:
                            time_remaining = False
                            break
                                
                            
                traject.add_station(current_station)
        
        # Update de toestand van de dienstregeling
        State.add_traject(traject)
                
    # Bereken de score van de gehele dienstregeling
    K: int = State.calculate_score()

    return State, K