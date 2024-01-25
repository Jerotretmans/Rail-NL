import sys
sys.path.append('../')
from helpers import read_csv_file
import random
sys.path.append('../classes')
from stations import Station
from traject import Traject
from dienstregeling import Regeling

def run_randalg():

    # Random aantal trajecten
    aantal_trajecten = random.randint(1, 7)

    # Maximale tijd per traject
    max_tijd_per_traject = random.randint(1, 120)

    # Minimale tijd per traject
    # min_tijd_per_traject = 1

    # Data lezen
    stations_data = read_csv_file('../../data/StationsHolland.csv')
    connections_data = read_csv_file('../../data/ConnectiesHolland.csv')

    # Maak stations object and connecties
    station_objects = {}
    for row in stations_data:
        station_name = row[0]
        station_objects[station_name] = Station(station_name)
    
    # Voeg een tweede station toe om er zeker van te zijn dat er altijd 1 verbinding is
    for row in connections_data:
        main_station_name = row[0]
        connected_station_name = row[1]
        time = row[2]
        station_objects[main_station_name].create_connection(connected_station_name, time)
        station_objects[connected_station_name].create_connection(main_station_name, time)
    # print(station_objects)

    # Maak een lijst trajecten
    trajects_list = []

    # Maak een set voor unieke verbindingen
    unieke_connections = set()

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
            # print(traject.station_counter)
            # if traject.station_counter > 0:
            #     max_tijd_per_traject = random.randint(1, 120)
            # print(traject)
            # Update the current station
            random_station = next_station
        
        # Add the constructed traject to the list of trajects
        trajects_list.append(traject)
    # random_station = (random.choice(stations_name_list))
    
    # print(random_station)

    for traject in trajects_list:
        #
        stations = traject.stations_in_traject
        for i in range(len(stations) - 1):
            connection = frozenset([stations[i].get_name(), stations[i+1].get_name()])
            unieke_connections.add(connection)


    p = len(unieke_connections) / 28
    # print(p)
    T = len(trajects_list)
    # print(T)
    Min = sum(traject.time for traject in trajects_list)
    # print(Min)
    # Bereken de score
    K = round(p * 10000 - (T * 100 + Min))
    
    # Print the details of each constructed traject
    # for traject in trajects_list:
    #     print(f"{traject.name}: {traject.get_names()} with total time {traject.time} minutes")

    # print(f"Score of the Regeling: {K}")

    return K

    # return score
        
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

