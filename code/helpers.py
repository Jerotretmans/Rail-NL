import csv
import json

def read_csv_file(filename) -> None:
    rows = []
    with open(filename) as file:
        stations = csv.reader(file)
        header = next(stations)
        for row in stations:
            rows.append(row)
    return rows

def read_GeoJSON_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data