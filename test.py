import csv
rows = []
with open('StationsHolland.csv') as stations_file:
    stations = csv.reader(stations_file)
    header = next(stations)
    for row in stations:
        rows.append(row)

print(header)
print(rows)
