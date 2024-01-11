# Random Algorithm
import sys
sys.path.append('../')
from helpers import read_csv_file
import random
from station
from traject import Traject
from dienstregeling import Regeling

if __name__ == "__main__":

    # Lees de locatue en connecties tussen stations vanuit csn bestanden
    stations = read_csv_file('../../data/StationsHolland.csv')
    connections = read_csv_file('../../data/ConnectiesHolland.csv')

    stations_name_list = []

    for row in stations:
        station_name = row[0]
        stations_name_list.append(station_name)

    
    random_station = (random.choice(stations_name_list))
    station = Station('random_station')
    
    print(random_station)