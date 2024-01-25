import csv

def open_connectiesHolland():
    with open('ConnectiesHolland.csv') as connections_file:
        connections = csv.reader(connections_file)
        header = next(connections)
    print(connections)
    return connections

