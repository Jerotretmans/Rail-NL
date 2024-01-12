from helpers import read_csv_file
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


stations = read_csv_file('StationsHolland.csv')

names = []
x_coords = []
y_coords = []


for station in stations[1]:
    names.append(station[0])
    x_coords.append(station[2])
    y_coords.append(station[1])

print(names)
print(x_coords)
print(y_coords)

plt.scatter(x_coords, y_coords, color='blue')
plt.xlabel('Lengtebreedte')
plt.ylabel('Hoogtebreedte')

plt.grid(True)
plt.show()