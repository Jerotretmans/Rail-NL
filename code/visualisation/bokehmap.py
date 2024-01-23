import json
from itertools import cycle
import sys
sys.path.append('../')
sys.path.append('../classes')

import pandas as pd

from bokeh.models import GeoJSONDataSource, ColumnDataSource, Line
from bokeh.palettes import Category20
from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256

from helpers import read_GeoJSON_file, read_csv_file
from classes.dienstregeling import Regeling
from classes.stations import Station








# Start met maken van eigen GeoJSON bestand


my_stations = read_csv_file('../../data/StationsHolland.csv')
my_connections = read_csv_file('../../data/ConnectiesHolland.csv')

stations_dict = {}
stations_obj = []
# Voeg de coördinaten toe aan een dictionary
for row in my_stations:
    name = row[0]
    station = Station(name)
    stations_obj.append(station)
    x = float(row[2])
    y = float(row[1])
    station.add_location(x, y)
    stations_dict[name] = [x, y]
print(stations_dict)


# # Voeg de connecties toe aan een aparte dictionary
# for row in my_connections:
#     main_station = row[0]
#     connected_station = row[1]
#     time = row[2]

#     for station in stations_obj:
#         if station.get_name() == main_station:
#             connections_dict[connected_station] = True
#         elif station.get_name() == connected_station:
#             connections_dict[main_station] = True
    
# for station in stations_obj:
#     print(f"{connections_dict}")



# station1 = Station('Alkmaar')
# station2 = Station('Hoorn')
# connections_dict[station1] = station2
connections_dict = {}
for row in my_connections:
    station1 = Station(row[0])
    station2 = Station(row[1])
    time = row[2]
    connections_dict[station1] = station2

station1naam = station1.name
station2naam = station2.name
print(connections_dict)
    
line_features = []

# Itereer door de stations om lijnen te kunnen trekken
for station1, station2 in connections_dict.items():
        
    start_coords = stations_dict[station1.name]
    end_coords = stations_dict[station2.name]
    line_feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [start_coords, end_coords]
        },
        "properties": {
            "name": f"{station1.name} -> {station2.name}"
        }
    }
    line_features.append(line_feature)


# Maak een eigen GeoJSON object met lijneigenschappen van de connecties
my_geojson = {
    "type": "FeatureCollection",
    "features": line_features
}

# Specify the file path where you want to save the GeoJSON file
file_path = "../../data/connections.geojson"

# Write the GeoJSON data to the file using json.dump
with open(file_path, "w") as geojson_file:
    json.dump(my_geojson, geojson_file, indent=2)





# Load GeoJSON file
data = read_GeoJSON_file('../../data/provinces.geojson')

connection_data = read_GeoJSON_file('../../data/connections.geojson')

# Load csv files
stations = pd.read_csv('../../data/StationsHolland.csv')
connections = pd.read_csv('../../data/ConnectiesHolland.csv')
dienstregeling_obj = Regeling('DR1')

# Geef kleurtjes aan de provincies
color_cycle = cycle(Category20[20])
for i in range(len(data['features'])):
    data['features'][i]['properties']['Color'] = next(color_cycle)

# Creëer een GeoJSONDataSource voor de provincies
geo_source = GeoJSONDataSource(geojson=json.dumps(data))

# Creëer een GeoJSONDataSource voor de connecties
connection_geo_source = GeoJSONDataSource(geojson=json.dumps(connection_data))


# Tooltips setup
# TOOLTIPS = [('Provincie', '@Provincie')]

# Creëer figuur
p = figure(background_fill_color="lightgrey", tooltips=None)
p.patches('xs', 'ys', source=geo_source, line_color='black', color='Color', alpha=0.7)

# Plot station locations as circles
p.circle(x='x', y='y', size=5, color='black', alpha=1, source=stations.reset_index())

# Color mapper voor de trajecten
color_mapper = linear_cmap(field_name='index', palette=Viridis256, low=0, high=len(dienstregeling_obj.trajecten_in_regeling))








p.multi_line('xs', 'ys', line_color='blue', line_width=2, source=connection_geo_source)

show(p)