import csv
import json
from typing import Union

# Leest csv bestanden
def read_csv_file(filename) -> None:
    rows = []
    with open(filename) as file:
        stations = csv.reader(file)
        _ = next(stations) # Negeer de boevneste regel van het csv bestand
        for row in stations:
            rows.append(row)
    return rows

# Leest GeoJSON bestanden voor de visualisatie
def read_GeoJSON_file(filename: str) -> Union[dict, None]:
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def load_algorithms_dict() -> dict:
    return {'rd': 'random',\
            'gr': 'greedy',\
            'hc': 'hill climber',\
            'sa': 'simulated annealing',\
            'df': 'depth first',\
            'bf': 'breadth first'}