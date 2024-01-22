import json
from itertools import cycle
import sys
sys.path.append('../')

from bokeh.models import GeoJSONDataSource
from bokeh.palettes import Category20
from bokeh.plotting import figure, show
from bokeh.transform import linear_cmap
from bokeh.palettes import Viridis256

from helpers import read_csv_file, read_GeoJSON_file


# Load GeoJSON file
NL_provinces = '../../data/provinces.geojson'
with open(NL_provinces, 'r') as file:
    data = json.load(file)

stations = read_csv_file('../../data/StationsHolland.csv')
connections = read_csv_file('../../data/ConnectiesHolland.csv')

# Geef kleurtjes aan de provincies
color_cycle = cycle(Category20[20])
for i in range(len(data['features'])):
    data['features'][i]['properties']['Color'] = next(color_cycle)

# Create a GeoJSONDataSource from your GeoJSON data
geo_source = GeoJSONDataSource(geojson=json.dumps(data))

# Tooltips setup (assuming 'OrganisationName' is a property in your GeoJSON)
TOOLTIPS = [('Organisation', '@OrganisationName')]

# Creëer figuur
p = figure(background_fill_color="lightgrey", tooltips=TOOLTIPS)
p.patches('xs', 'ys', source=geo_source, line_color='black', color='Color', alpha=0.7)

# Create a color mapper for stations
# color_mapper = linear_cmap(field_name='index', palette=Viridis256, low=0, high=len(stations))

# Plot station locations as circles
# p.circle(x='x', y='y', size=15, color=color_mapper, alpha=0.7, source=stations.reset_index())

show(p)