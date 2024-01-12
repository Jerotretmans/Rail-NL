import csv
rows = []
with open('StationsHolland.csv') as stations_file:
    stations = csv.reader(stations_file)
    header = next(stations)
    for row in stations:
        rows.append(row)
print(header)
print(rows)

rows = []
with open('ConnectiesHolland.csv') as connections_file:
    connections = csv.reader(connections_file)
    header = next(connections)
    for row in connections:
        rows.append(row)
print(header)
print(rows)
