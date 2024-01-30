import sys
from typing import Dict, List, Any

sys.path.append('../')
from .stations import Station

from algorithms.randalg import run_randalg
from algorithms.greedy import run_greedy
from algorithms.depth_first import run_depth_first
from algorithms.breadth_first import run_breadth_first
from algorithms.hill_climber import run_hill_climber

class Algorithm:

    def __init__(self, name: str, stations_data: List[List[str]], connections_data: List[List[str]],
                max_trajecten: int, max_tijd_traject: int, alle_connecties: int):
        self.name: str = name
        self.station_objects: Dict[str, Station] = {}
        self.stations_data: List[List[str]] = stations_data
        self.connections_data: List[List[str]] = connections_data
        self.max_trajecten: int = max_trajecten
        self.max_tijd_traject: int = max_tijd_traject
        self.alle_connecties = alle_connecties
        self.traject_list = []

    def create_station_objects(self) -> Dict[str, Station]:
        for row in self.stations_data:
            station_name: str = row[0]
            self.station_objects[station_name] = Station(station_name)

        # Voeg een tweede station toe om er zeker van te zijn dat er altijd 1 verbinding is
        for row in self.connections_data:
            main_station_name: str = row[0]
            connected_station_name: str = row[1]
            time: int = row[2]
            self.station_objects[main_station_name].create_connection(connected_station_name, time)
            self.station_objects[connected_station_name].create_connection(main_station_name, time)

        return self.station_objects
    
    
    def run_algorithm(self, algorithm_instance: Any) -> Any:
        self.algorithm_instance = algorithm_instance
        if self.name == 'random':
            return run_randalg(algorithm_instance)
            
        elif self.name == 'greedy':
            return run_greedy(algorithm_instance)

        elif self.name == 'hill climber':
            return run_hill_climber(algorithm_instance)

        elif self.name == 'depth first':
            return run_depth_first(algorithm_instance)

        elif self.name == 'breadth first':
            return run_breadth_first(algorithm_instance)
        
        else:
            raise AssertionError ("Geen valide naam!")
            
    

    def run_algorithm_N_times(self, N, algorithm_instance):
        scores_list: List[int] = []
        n_runs = 0
        self.algorithm_instance = algorithm_instance
        for _ in range(N):
            print(f"run: {n_runs}")
            score = self.run_algorithm(self.algorithm_instance)
            scores_list.append(score)
            n_runs += 1
        return scores_list