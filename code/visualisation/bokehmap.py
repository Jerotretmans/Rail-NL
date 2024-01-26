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

Usage: 'python3 bokehmap.py holland' or 'python3 bokehmap.py nl' 
"""

# Lees de csv bestanden d.m.v. eigen functie voor de dictionaries
my_stations = read_csv_file('../../data/StationsHolland.csv')
my_stations_nl = read_csv_file('../../data/StationsNationaal.csv')
my_connections = read_csv_file('../../data/ConnectiesHolland.csv')
my_connections_nl = read_csv_file('../../data/ConnectiesNationaal.csv')


# Verzeker het correcte gebruik van de code
assert len(sys.argv) == 2, "Usage: 'python3 bokehmap.py holland' or 'python3 bokehmap.py nl'" 


# Initialiseer dicts voor stationslocaties en voor connecties tussen de locaties
stations_dict = {}
connections_dict = {}


# Voeg locaties van stations toe aan stations_dict
def fill_stations_dict(region_file):
    for row in region_file:
        name = row[0]
        x = float(row[2])
        y = float(row[1])
        stations_dict[name] = [x, y]


# Voeg de connecties toe aan connections_dict
def fill_connections_dict(region_file):
    for row in region_file:
        station1 = Station(row[0])
        station2 = Station(row[1])
        time = row[2]
        connections_dict[station1] = station2


# Implementeer de visualisatie voor regio Holland of op nationaal niveau
if sys.argv[1].lower() == 'holland':
    fill_stations_dict(my_stations)
    fill_connections_dict(my_connections)
    data = read_GeoJSON_file('../../data/holland.geojson')
    pd_stations = pd.read_csv('../../data/StationsHolland.csv')
elif sys.argv[1].lower() == 'nl':
    fill_stations_dict(my_stations_nl)
    fill_connections_dict(my_connections_nl)
    data = read_GeoJSON_file('../../data/nl.geojson')
    pd_stations = pd.read_csv('../../data/StationsNationaal.csv')
else:
    raise AssertionError ("Usage: 'python3 bokehmap.py holland' or 'python3 bokehmap.py nl'")



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
        },
        "tooltip": f"{station1.name} -> {station2.name}"
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



# Laad het GeoJSON bestand van de connecties
connection_data = read_GeoJSON_file('../../data/connections.geojson')


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

# Voeg connecties tussen stations toe
p.multi_line('xs', 'ys', line_color='red', line_width=2, source=connection_geo_source)

# Plot station locaties als stippen
p.circle(x='x', y='y', size=6, color='black', alpha=1, source=pd_stations.reset_index())

# Color mapper voor de trajecten
dienstregeling_obj = Regeling('DR1')
color_mapper = linear_cmap(field_name='index', palette=Viridis256, low=0, high=len(dienstregeling_obj.trajecten_in_regeling))

# Display de plot in een browser
show(p)

