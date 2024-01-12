import csv

def read_file(filename) -> None:

    rows = []
    with open(filename) as file:
        stations = csv.reader(file)
        header = next(stations)
        for row in stations:
            rows.append(row)
    
    return header, rows

def open_connectiesHolland():
    with open('ConnectiesHolland.csv') as connections_file:
        connections = csv.reader(connections_file)
        header = next(connections)
    print(connections)
    return connections
