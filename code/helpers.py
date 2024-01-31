import csv
import json
from typing import Union

# Leest csv bestanden
def read_csv_file(filename) -> None:
    rows = []
    with open(filename) as file:
        stations = csv.reader(file)
        _ = next(stations) # Negeer de bovenste regel van het csv bestand
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
            'bf': 'breadth first',\
            'sa': 'simulated annealing',\
            'br': 'bizzey',\
            'qr': 'rustaaahg'}

# Schrijft een csv bestand van een state
def export_output(csv_file_path):

    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Header
        csv_writer.writerow(["train", "stations"])
        csv_writer.writerow(["trajecten in regeling"])
        csv_writer.writerow(["score"])
        
    print(f"Output has been exported to {csv_file_path}")