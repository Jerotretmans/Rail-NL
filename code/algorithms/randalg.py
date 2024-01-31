import sys
sys.path.append('../')
sys.path.append('/classes')

import random

from classes.traject import Traject
from classes.dienstregeling import Regeling
from classes.stations import Station


"""
Implementatie van het random algoritme. Onderaan zijn twee algoritmes gedefinieerd
waarbij 2 van de startstations vast staan: 'bizzey' begint bij drukke stations en
'rustaaahg' begint bij rustige stations. 
"""

twee_start_stations = False

def start_stations_bizzey():
    """
    Returnt de startstations de eerste twee 'bizzey' trajecten.
    """
    station_names_bizzey = ["Amsterdam Sloterdijk", "Leiden Centraal"]
    return station_names_bizzey


def start_stations_rustaaahg():
    """
    Returnt de startstations de eerste twee 'rustaaahg' trajecten.
    """
    station_names_bizzey = ["Den Helder", "Dordrecht"]
    return station_names_bizzey

# Eenmalige run van het random algoritme
def run_randalg(algorithm_instance, regio, aantal_trajecten) -> int:

    # Roep een toestand op waarin de dienstregeling zich verkeert
    State = Regeling(regio)

    # Random aantal trajecten
    aantal_trajecten: int = random.randint(1, State.max_trajecten)

    # Maximale tijd per traject
    max_tijd_per_traject: int = random.randint(1, 120)

    for i in range(aantal_trajecten):
        # random start station
        random_station_name: str = random.choice(list(algorithm_instance.station_objects.keys()))
        random_station: Station = algorithm_instance.station_objects[random_station_name]
        
        # begin een traject
        traject = Traject(f"Traject_{i+1}", regio)
        
        # begin met het maken van een traject
        traject.add_station(random_station)
        
        # Voeg een eerste verbinding toe zodat er nooit 0 verbindingen zijn
        connected_stations = list(random_station.connections.keys())
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

def run_randalg_bizzey(algorithm_instance, regio, aantal_trajecten):
    
    bizzey_start_stations = start_stations_bizzey()

    State = Regeling(regio)

    aantal_trajecten: int = random.randint(2, State.max_trajecten)

    max_tijd_per_traject: int = random.randint(1, 120)

    for i in range(aantal_trajecten):
        # Use the bizzey start stations for the first two trajectories
        if i < len(bizzey_start_stations):
            station_name = bizzey_start_stations[i]
            random_station = algorithm_instance.station_objects.get(station_name)
        else:
        # Random start station for subsequent trajectories
            random_station_name = random.choice(list(algorithm_instance.station_objects.keys()))
            random_station = algorithm_instance.station_objects[random_station_name]

        traject: Traject = Traject(f"Bizzey_Traject_{i+1}", regio)

        traject.add_station(random_station)

        connected_stations = list(random_station.connections.keys())
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
    K = State.calculate_score()
    return State, K

def run_randalg_rustaaahg(algorithm_instance, regio):
    rustaaahg_start_stations = start_stations_rustaaahg()

    State = Regeling(regio)

    aantal_trajecten: int = random.randint(2, State.max_trajecten)

    max_tijd_per_traject: int = random.randint(1, 120)

    for i in range(aantal_trajecten):
        if i < len(rustaaahg_start_stations):
            station_name = rustaaahg_start_stations[i]
            random_station = algorithm_instance.station_objects.get(station_name)
        else:
            random_station_name = random.choice(list(algorithm_instance.station_objects.keys()))
            random_station = algorithm_instance.station_objects[random_station_name]

        traject: Traject = Traject(f"Rustaaahg_Traject_{i+1}", regio)

        traject.add_station(random_station)

        connected_stations = list(random_station.connections.keys())
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
    K = State.calculate_score()
    return State, K
