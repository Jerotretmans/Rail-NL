import json
from itertools import cycle
import sys
sys.path.append('../')
sys.path.append('../classes')

import pandas as pd

from bokeh.models import GeoJSONDataSource
from bokeh.palettes import Category20
from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256

from helpers import read_GeoJSON_file, read_csv_file
from classes.dienstregeling import Regeling
from classes.stations import Station

"""
Visualisatie van de stations en bijbehorende connecties binnen regio Holland 
en op landelijk niveau. Gebruik makende van Bokeh als visualisatietool en 
een eigen geschreven GeoJSON bestand voor de connecties.
"""

# Lees de csv bestanden voor 
my_stations = read_csv_file('../../data/StationsHolland.csv')
my_connections = read_csv_file('../../data/ConnectiesHolland.csv')

class Visualise:

    def __init__(self):
        pass


# Voeg de coördinaten toe aan een dictionary
stations_dict = {}
for row in my_stations:
    name = row[0]
    station = Station(name)
    x = float(row[2])
    y = float(row[1])
    stations_dict[name] = [x, y]


# Voeg de connecties toe aan een aparte dictionary
connections_dict = {}
for row in my_connections:
    station1 = Station(row[0])
    station2 = Station(row[1])
    time = row[2]
    connections_dict[station1] = station2


# Itereer door de stations om lijnen te kunnen trekken
line_features = []
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

# Geef aan waar het GeoJSON bestand naartoe moet
file_path = "../../data/connections.geojson"

# Schrijf het GeoJSON bestand met json.dump
with open(file_path, "w") as geojson_file:
    json.dump(my_geojson, geojson_file, indent=2)



# Laad GeoJSON bestanden
data = read_GeoJSON_file('../../data/provinces.geojson')
connection_data = read_GeoJSON_file('../../data/connections.geojson')

# Laadd csv bestanden
stations = pd.read_csv('../../data/StationsHolland.csv')
connections = pd.read_csv('../../data/ConnectiesHolland.csv')


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

# Voeg grenzen van provincies toe
p.patches('xs', 'ys', source=geo_source, line_color='black', color='Color', alpha=0.7)

# Plot station locations as circles
p.circle(x='x', y='y', size=5, color='black', alpha=1, source=stations.reset_index())

# Color mapper voor de trajecten
dienstregeling_obj = Regeling('DR1')
color_mapper = linear_cmap(field_name='index', palette=Viridis256, low=0, high=len(dienstregeling_obj.trajecten_in_regeling))

# Voeg connecties tussen stations toe
p.multi_line('xs', 'ys', line_color='blue', line_width=2, source=connection_geo_source)

show(p)