import sys
sys.path.append('/classes')

import random

from classes.traject import Traject
from classes.dienstregeling import Regeling


"""
Implementatie van het random algoritme.
"""

def set_begin_stations_bizzey():
    pass

def set_begin_stations_rustaaahg():
    pass

# Eenmalige run van het random algoritme
def run_randalg(algorithm_instance, regio):

    # Initialiseer een toestand van de dienstregeling
    state = Regeling()

    # Stel maxima in op basis van de regio
    if regio == 'h':
        state.max_trajecten = 7
        # traject.max_tijd = 120
    elif regio == 'nl':
        state.max_trajecten = 20
        # traject.max_tijd = 180
    else:
        raise AssertionError ("Geen valide naam!")

    # Random aantal trajecten
    aantal_trajecten = random.randint(1, 7)

    # Maximale tijd per traject
    max_tijd_per_traject = random.randint(1, 120)

    for i in range(aantal_trajecten):
        # random start station
        random_station_name = random.choice(list(algorithm_instance.station_objects.keys()))
        random_station = algorithm_instance.station_objects[random_station_name]
        
        # begin een traject
        traject = Traject(f"Traject_{i+1}")
        
        # begin met het maken van een traject
        traject.add_station(random_station)
        
        # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
        connected_stations = list(random_station.connections.keys())
        if connected_stations:  # Ensure there is at least one connected station
            next_station_name = random.choice(connected_stations)
            next_station = algorithm_instance.station_objects[next_station_name]
            traject.add_station(next_station)
            random_station = next_station
        
        # blijf stations toevoegen totdat de maximale tijd is bereikt
        while traject.time < max_tijd_per_traject:
            connected_stations = list(random_station.connections.keys())
            if not connected_stations:
                break
            
            # Voeg random station aan traject
            next_station_name = random.choice(connected_stations)
            next_station = algorithm_instance.station_objects[next_station_name]
            
            # Check de tijd voordat je weer een station toevoegt 
            additional_time = int(random_station.connections[next_station_name])
            if traject.time + additional_time > max_tijd_per_traject:
                break
            
            # voeg station toe
            traject.add_station(next_station)
            random_station = next_station
        
        # Update de toestand van de dienstregeling
        state.add_traject(traject)
    

    # Bereken de score van de gehele dienstregeling
    K = state.calculate_score()

    return state, K


def run_randalg_bizzey(algorithm_instance: Regeling):

    set_begin_stations_bizzey()

    run_randalg()

    pass

def run_randalg_rustaaahg(algorithm_instance: Regeling):

    set_begin_stations_rustaaahg()

    run_randalg()

    pass