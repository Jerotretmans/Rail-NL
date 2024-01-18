import sys
sys.path.append('../')
from helpers import read_csv_file
import random
from stations import Station
from traject import Traject
from dienstregeling import Regeling

if __name__ == "__main__":

    # Random aantal trajecten
    aantal_trajecten = random.randint(1, 7)

    # Maximale tijd per traject
    max_tijd_per_traject = 120 

    # Data lezen
    stations_data = read_csv_file('../../data/StationsHolland.csv')
    connections_data = read_csv_file('../../data/ConnectiesHolland.csv')

    # Initialize station objects and set connections
    station_objects = {}
    for row in stations_data:
        station_name = row[0]
        station_objects[station_name] = Station(station_name)
    
    for row in connections_data:
        main_station_name = row[0]
        connected_station_name = row[1]
        time = row[2]
        station_objects[main_station_name].create_connection(connected_station_name, time)
        station_objects[connected_station_name].create_connection(main_station_name, time)

    # Initialize a list to hold the generated trajects
    trajects = []

    for i in range(aantal_trajecten):
        # Choose a random station to start the traject
        random_station_name = random.choice(list(station_objects.keys()))
        random_station = station_objects[random_station_name]
        
        # Initialize a new traject
        traject = Traject(f"Traject_{i+1}")
        
        # Start constructing the traject from the random station
        traject.add_station(random_station)
        
        # Continue adding stations until the maximum time is reached
        while traject.time < max_tijd_per_traject:
            connected_stations = list(random_station.connections.keys())
            if not connected_stations:
                break  # No more connected stations to add
            
            # Choose a random connected station to add to the traject
            next_station_name = random.choice(connected_stations)
            next_station = station_objects[next_station_name]
            
            # Check the time before actually adding the station to ensure it doesn't exceed the max time
            additional_time = int(random_station.connections[next_station_name])
            if traject.time + additional_time > max_tijd_per_traject:
                break  # Adding this station would exceed the max time, so end this traject
            
            # Add the station to the traject
            traject.add_station(next_station)
            print(traject.station_counter)
            if traject.station_counter > 0:
                max_tijd_per_traject = random.randint(1, 120)
            # print(traject)
            # Update the current station
            random_station = next_station
        
        # Add the constructed traject to the list of trajects
        trajects.append(traject)
    # random_station = (random.choice(stations_name_list))
    
    print(random_station)




    
    # Print the details of each constructed traject
    for traject in trajects:
        print(f"{traject.name}: {traject.get_names()} with total time {traject.time} minutes")
