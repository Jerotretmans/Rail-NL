import csv
import json

# Leest csv bestanden
def read_csv_file(filename) -> None:
    rows = []
    with open(filename) as file:
        stations = csv.reader(file)
        header = next(stations) # Negeer de boevneste regel van het csv bestand
        for row in stations:
            rows.append(row)
    return rows

# Leest GeoJSON bestanden voor de visualisatie
def read_GeoJSON_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
