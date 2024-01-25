from stations import Station
from traject import Traject
import sys
sys.path.append('../')
from helpers import read_csv_file
import csv
from collections import Counter

class Regeling:
    """
    Een verzameling trajecten die samen zo veel mogelijk stations bereikt in zo min 
    mogelijk tijd, en waar elke verbinding gereden wordt. Score: K = p*10000 - (T*100 + Min)

    Constraint: max 7 trajecten
    """
    def __init__(self, name) -> None:
        self.name = name
        # self.current_traject = None
        self.trajecten_in_regeling = []
        self.traject_counter = 0
        self.total_time = 0

        self.p = 0
        self.T = 0
        self.Min = 0

    def add_traject(self, new_traject) -> None:
        if self.traject_counter < 8:
            self.trajecten_in_regeling.append(new_traject)
            self.traject_counter += 1
            # print(f"totale tijd nieuwe traject: {new_traject.time}")
            self.total_time += new_traject.time
            # self.current_traject = new_traject
        else:
            print("maximaal aantal trajecten bereikt")

    # def __repr__(self):
    #     return f"{self.name}: {self.trajecten_in_regeling}, Time: {self.total_time}"

    def calculate_p(self):
        unique_stations = set()
        for traject in self.trajecten_in_regeling:
            for station in traject.get_names():
                unique_stations.add(station)

        stations_reached = (len(unique_stations))
        p = stations_reached / 22
        return p
        

    def calculate_T(self):
        # returnt aantal trajecten
        t = self.traject_counter
        return t

    def calculate_min(self):
        min = self.total_time
        return min

    def calculate_score(self):
        p = self.calculate_p()
        # print(p)
        t = self.calculate_T()
        # print(t)
        min = self.calculate_min()
        # print(min)
        
        K = p*10000 - (t*100 + min)
        return K
    
    
    def export_output(self):
        csv_file_path = '../../output.csv'  
        
        with open(csv_file_path, 'w', newline='') as csvfile:
            # Create a CSV writer
            csv_writer = csv.writer(csvfile)

            # Write the header
            csv_writer.writerow(["train", "stations"])
            csv_writer.writerow(self.trajecten_in_regeling)
            csv_writer.writerow(["score",  self.calculate_score()])
        
        print(f"Output has been exported to {csv_file_path}")



if __name__ == "__main__":
    """
    Test functie voordat we in main.py bezig gaan.
    """

    # Lees verbindingen van CSV bestand
    connections = read_csv_file('../../data/ConnectiesHolland.csv')
    
    test_stations = []
    station1 = Station('Hoorn')
    station2 = Station('Alkmaar')
    station3 = Station('Den Helder')
    station4 = Station('Gouda')
    station5 = Station('Alkmaar')

    test_stations.append(station1)
    test_stations.append(station2)
    test_stations.append(station3)
    test_stations.append(station4)
    test_stations.append(station5)

    for row in connections:
        main_station = row[0]
        connected_station = row[1]
        time = row[2]

        for station in test_stations:
            if station.name == main_station:
                station.create_connection(connected_station, time)
            elif station.name == connected_station:
                station.create_connection(main_station, time)
    
    name = "Train_1"
    traject1 = Traject(name)
    
    for station in test_stations:
        print(f"Name: {station.get_name()}")
        traject1.add_station(station)

    regeling1 = Regeling("Regeling_1")
    regeling1.add_traject(traject1)
    # print(regeling1.calculate_T())
    regeling1.export_output()
    # print(regeling1.calculate_score())


    
    
