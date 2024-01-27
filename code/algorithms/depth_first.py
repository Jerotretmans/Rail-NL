import sys
import random

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
def run_depth_first(algorithm_instance):

    # bepaal max aantal trajecten en max tijd
    aantal_trajecten = 5
    max_tijd_per_traject = 120
    specific_starts = {"Traject_1": "Gouda", "Traject_2": "Dordrecht"}
    visited_start_station = set()
    all_visited_stations = set()


    # Roep een toestand op waarin de dienstregeling zich verkeert
    State = Regeling()    
    
    # Maak elk traject
    for i in range(aantal_trajecten):
        # Maak een lege set om alle bezocte stations te onthouden
        visited_stations = set()
        if f"Traject_{i+1}" in specific_starts:
        # Use the specific starting station
            random_station_name = specific_starts[f"Traject_{i+1}"]
            random_station = algorithm_instance.station_objects[random_station_name]
        else:
        # Kies een random station om te beginnen
            while True:
                random_station_name = random.choice(list(algorithm_instance.station_objects.keys()))
                random_station = algorithm_instance.station_objects[random_station_name]
                if random_station not in visited_start_station:
                    visited_start_station.add(random_station)
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
                all_visited_stations.add(current_station) 
                    # Voeg het station toe aan het traject
                traject.add_station(current_station)
                    
                    # Ga over de verbonden stations
                for next_station_name, time_to_next in current_station.connections.items():
                        # Kijk of een verbonden station al bezocht is en zo niet dan...
                    if next_station_name not in visited_stations and next_station_name:
                        next_station = algorithm_instance.station_objects[next_station_name]
                        time_to_next_int = int(time_to_next)
                            # Check of het toevoegen van die connectie niet de maximale tijd overschrijdt 
                        if current_time + time_to_next_int <= max_tijd_per_traject:
                            stack.append((next_station, current_time + time_to_next_int))
                            # als het toevoegen de tijd zou overschrijden break dan uit de loop en de while loop
                        else:
                            time_remaining = False
                            break
                                
                            
                traject.add_station(current_station)
        
        # Update de toestand van de dienstregeling
        State.add_traject(traject)
                
    # Bereken de score van de gehele dienstregeling
    K = State.calculate_score(State.traject_list)

    return K


# Run het Depth First algoritme meerdere keren
def run_df_N_times(N):
    scores_list = []
    
    for _ in range(N):
        score = run_depth_first()
        scores_list.append(score)

    return scores_list


if __name__ == "__main__":

    # Verzeker het correcte gebruik van de code
    assert len(sys.argv) == 2, "Usage: 'python3 randalg.py holland' or 'python3 randalg.py nl'"

    # Data lezen
    if sys.argv[1].lower() == 'holland':
        stations_data = read_csv_file('../../data/StationsHolland.csv')
        connections_data = read_csv_file('../../data/ConnectiesHolland.csv')
    elif sys.argv[1].lower() == 'nl':
        stations_data = read_csv_file('../../data/StationsNationaal.csv')
        connections_data = read_csv_file('../../data/ConnectiesNationaal.csv')
    else:
        raise AssertionError ("Usage: 'python3 bokehmap.py holland' or 'python3 bokehmap.py nl'")

    # Vraag om een hoeveelheid runs van het algoritme
    try:
        N = int(input("Hoe vaak moet het algoritme worden uitgevoerd "))
    # Accepteer alleen integers
    except ValueError:
        print("Alleen hele getallen a.u.b.")

    # Run het algoritme hoe vaak de gebruiker opgeeft
    scores = run_df_N_times(N)
    high_score = max(scores)
    print(f"Highest score: {high_score}")
