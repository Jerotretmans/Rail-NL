import sys
sys.path.append('../')
from helpers import read_csv_file
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


stations = read_csv_file('../../data/StationsHolland.csv')

names = []
x_coords = []
y_coords = []

for station in stations[1]:
    names.append(station[0])
    x_coords.append(station[2])
    y_coords.append(station[1])

x_list = [float(x) for x in x_coords]
y_list = [float(y) for y in y_coords]

plt.scatter(x_list, y_list, color='blue')
plt.xlim(4.0, 5.4)
plt.xlabel('Lengtegraden')
plt.ylabel('Breedtegraden')

plt.grid(True)
plt.tight_layout()
plt.show()