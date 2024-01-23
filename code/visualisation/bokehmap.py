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

from helpers import read_GeoJSON_file
from classes.dienstregeling import Regeling


# Load GeoJSON file
data = read_GeoJSON_file('../../data/provinces.geojson')

# Load csv files
stations = pd.read_csv('../../data/StationsHolland.csv')
connections = pd.read_csv('../../data/ConnectiesHolland.csv')
dienstregeling_obj = Regeling('DR1')

# Geef kleurtjes aan de provincies
color_cycle = cycle(Category20[20])
for i in range(len(data['features'])):
    data['features'][i]['properties']['Color'] = next(color_cycle)

# Create a GeoJSONDataSource from your GeoJSON data
geo_source = GeoJSONDataSource(geojson=json.dumps(data))

# Tooltips setup
TOOLTIPS = [('Provincie', '@Provincie')]

# Creëer figuur
p = figure(background_fill_color="lightgrey", tooltips=TOOLTIPS)
p.patches('xs', 'ys', source=geo_source, line_color='black', color='Color', alpha=0.7)

# Color mapper voor de trajecten
color_mapper = linear_cmap(field_name='index', palette=Viridis256, low=0, high=len(dienstregeling_obj.trajecten_in_regeling))

# Plot station locations as circles
p.circle(x='x', y='y', size=5, color='black', alpha=1, source=stations.reset_index())

my_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [longitude, latitude]  # Replace with actual coordinates
            },
            "properties": {
                "name": "Your Location",
                "description": "Some description about the location"
            }
        }
        # You can add more features as needed
    ]
}

# Specify the file path where you want to save the GeoJSON file
file_path = "../../data/connections.geojson"

# Write the GeoJSON data to the file using json.dump
with open(file_path, "w") as geojson_file:
    json.dump(my_geojson, geojson_file, indent=2)

show(p)