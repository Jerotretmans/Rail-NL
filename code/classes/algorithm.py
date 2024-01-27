import sys
sys.path.append('../')

from .stations import Station

from ..algorithms.randalg import run_randalg
# from ..algorithms.greedy import run_greedy
# from ..algorithms.hill_climber import run_hill_climber
from ..algorithms.depth_first import run_depth_first
# from ..algorithms.breadth_first import run_breadth_first

from ..helpers import read_csv_file

class Algorithm:

    def _init_(self, name, stations_data, connections_data):
        self.name = name
        self.station_objects = {}
        self.stations_data = stations_data
        self.connections_data = connections_data

    def create_station_objects(self):
        for row in self.stations_data:
            station_name = row[0]
            self.station_objects[station_name] = Station(station_name)

        # Voeg een tweede station toe om er zeker van te zijn dat er altijd 1 verbinding is
        for row in self.connections_data:
            main_station_name = row[0]
            connected_station_name = row[1]
            time = row[2]
            self.station_objects[main_station_name].create_connection(connected_station_name, time)
            self.station_objects[connected_station_name].create_connection(main_station_name, time)

        return self.station_objects
    
    
    def run_algorithm(self, algorithm_instance):
        self.algorithm_instance = algorithm_instance
        if self.name == 'random':
            run_randalg(algorithm_instance)
        elif self.name == 'greedy':
            # run_greedy()
            pass
        elif self.name == 'hill climber':
            # run_hill_climber()
            pass
        elif self.name == 'depth first':
            # run_depth_first(df_object)
            pass
        elif self.name == 'breadth first':
            # run_breadth_first()
            pass
        else:
            raise AssertionError ("Geen valide naam!")
    

    def run_algorithm_N_times(self, N):
        scores_list = []
        for _ in range(N):
            score = self.run_algorithm(self.algorithm_instance)
            scores_list.append(score)

        return scores_list