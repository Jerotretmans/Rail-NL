import sys
sys.path.append('../')
from helpers import read_csv_file
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg

background_image = mpimg.imread('../../docs/Nederland.jpg')

stations = read_csv_file('../../data/StationsNationaal.csv')

names = []
x_coords = []
y_coords = []

for station in stations:
    names.append(station[0])
    x_coords.append(station[2])
    y_coords.append(station[1])

x_list = [float(x) for x in x_coords]
y_list = [float(y) for y in y_coords]

y_min, y_max = 50.6, 53.7

plt.imshow(background_image, zorder=0, extent=[3.2, 7.35, y_min, y_max], aspect='auto')
plt.scatter(x_list, y_list, color='blue')
plt.xlim(3.2, 7.2)
plt.ylim(y_min, y_max)
plt.xlabel('Lengtegraden')
plt.ylabel('Breedtegraden')

plt.yticks([i for i in range(int(y_min), int(y_max)+1, 1)])
plt.tick_params(axis='y', which='both', labelsize=10)

plt.grid(True)
plt.tight_layout()
plt.show()