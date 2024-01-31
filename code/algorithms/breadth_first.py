from classes.traject import Traject
from classes.dienstregeling import Regeling
from .depth_first import choose_start_station

"""
Implementatie van het Breadth First algoritme. Om dit algoritme aan te roepen
kan je dit script runnen.

Usage: 'python3 breadth_first.py holland' or 'python3 breadth_first.py nl' 
"""
# Maken van trajecten voor breadth_first algoritme
def compute_trajectory(algorithm_instance, start_station, all_visited_stations, traject_counter, regio) -> Traject:
    visited_stations = set()
    stack = [(start_station, 0)]
    trajectory = Traject(f"Traject_{traject_counter}", regio)
    time_remaining = True
    used_connections = set()

    # Loop totdat de stack leef is of de tijd op is
    while stack and time_remaining:
        current_station, current_time = stack.pop(0)

        # Check of het station niet al bereikt is
        if current_station not in visited_stations:
            
            # Voeg het station toe aan bezochte stations
            visited_stations.add(current_station)
            all_visited_stations.add(current_station)

            # Voeg het station toe aan het traject
            trajectory.add_station(current_station)

            # Doorzoek de volgende stations vanaf het huidige
            for next_station_name, time_to_next in current_station.connections.items():
                
                # Check of het volgende station nog niet bezocht is
                if next_station_name not in visited_stations:
                    next_station = algorithm_instance.station_objects[next_station_name]
                    time_to_next_int: int = int(time_to_next)

                    # Check of het toevoegen van een connectie niet te tijd overschrijd
                    if current_time + time_to_next_int <= trajectory.max_tijd:

                        # Voeg de connectie toe aan de gebruikte connecties
                        if current_station.name < next_station_name:
                            used_connections.add((current_station.name, next_station_name))
                        else:
                            used_connections.add((next_station_name, current_station.name))
                            
                        # Voeg de connectie toe aan de stack    
                        stack.append((next_station, current_time + time_to_next_int))
                    else:
                        time_remaining = False
                        break

    # Return traject en gebruike connecties    
    return trajectory, used_connections

# Eenmalig runnen van het breadth_first algoritme
def run_breadth_first(algorithm_instance, regio, aantal_trajecten):
    visited_start_station = set()
    all_possible_connections = {(station1, algorithm_instance.station_objects[station2]) for station1 in algorithm_instance.station_objects.values() for station2 in station1.connections}
    used_connections = set()
    traject_counter = 1

    # Maak een state
    state = Regeling(regio)

    # Blijf trajecten maken totdat alle connecties zijn gereden
    while used_connections != all_possible_connections:

        # Kies een start station
        start_station = choose_start_station(algorithm_instance, visited_start_station)
        visited_start_station.add(start_station)

        # Maak een Traject
        trajectory, trajectory_used_connections = compute_trajectory(algorithm_instance, start_station, used_connections, traject_counter, regio)

        # Voeg de connecties toe
        used_connections.update(trajectory_used_connections)
        
        # Update traject counter om aantal trajecten bij te houden voor de benaming
        traject_counter += 1

        # Voeg het traject toe aan de dienstregeling
        state.add_traject(trajectory)

        # Zorg dat je het maximaal aantal trajecten niet overschrijdt en max anders voor nl voor aanzienlijk betere scores
        if regio == 'h':
            if len(state.traject_list) >= state.max_trajecten:
                break
        if regio == 'nl':
            if len(state.traject_list) >= 11 or len(state.traject_list) >= state.max_trajecten:
                break

    # Bereken de score en return de score en state
    score = state.calculate_score()
    return state, score