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


# Berekent de kwaliteitsscore van de gehele dienstregeling
def calculate_score(traject_list):
    unique_connections = set()
    traject_counter = 0
    minutes = 0

    # Houd de variabelen bij
    for traject in traject_list:
        traject_counter += 1
        minutes += traject.time
        stations = traject.stations_in_traject

        for i in range(len(stations) - 1):
            connection = frozenset([stations[i].get_name(), stations[i+1].get_name()])
            unique_connections.add(connection)

    # Stel variabelen in
    p = len(unique_connections) / 28
    print(f"p = {p}")
    T = traject_counter
    print(f"T = {T}")
    Min = minutes
    print(f"Min = {Min}")

    # Bereken de score
    K = round(p * 10000 - (T * 100 + Min))     
    return K

