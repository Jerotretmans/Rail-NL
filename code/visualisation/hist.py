import sys
sys.path.append('../')
sys.path.append('../classes')
sys.path.append('../algorithms')

from helpers import read_csv_file

from dienstregeling import Regeling
from algorithm import Algorithm

from randalg import run_randalg
from depth_first import run_depth_first

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm


"""
Maakt een histogram van de scores van verschillende algoritmes.  
"""
description = """
Usage: 'python3 hist.py (algorithm)' waar (algorithm) een van de volgende afkortingen is:

rd for random
gr for greedy
hc for hill climber
bf for breadth first
df for depth first

Voorbeeld: 'python3 hist.py rd' 
"""

# Verzeker het correcte gebruik van de code
assert len(sys.argv) == 2, description

# Vraag om een hoeveelheid runs van het algoritme
try:
    N = int(input("Hoe vaak moet het algoritme worden uitgevoerd "))
# Accepteer alleen integers
except ValueError:
    print("Alleen hele getallen a.u.b.")


# Run algoritme op verzoek van de gebruiker
if sys.argv[1].lower() == 'rd':
    randalg_object = Algorithm('random', stations_data, connections_data)
    randalg_object.create_station_objects()
    alg_object = randalg_object

    # Vraag om een hoeveelheid runs van het algoritme
    try:
        N = int(input("Hoe vaak moet het algoritme worden uitgevoerd "))
    # Accepteer alleen integers
    except ValueError:
        print("Alleen hele getallen a.u.b.")

    # Run het algoritme hoe vaak de gebruiker opgeeft
    scores_list = randalg_object.run_algorithm_N_times(N, alg_object)
    algorithm = 'Random'
    algorithm_abrev = 'rd'
elif sys.argv[1].lower() == 'gr':
    # scores_list = run_alg_N_times(N)
    algorithm = 'Greedy'
    algorithm_abrev = 'gr'
elif sys.argv[1] == 'hc':
    # scores_list = run_alg_N_times(N)
    algorithm = 'Hill Climber'
    algorithm_abrev = 'hc'
elif sys.argv[1].lower() == 'bf':
    # scores_list = run_randalg_N_times(N)
    algorithm = 'Breadth First'
    algorithm_abrev = 'bf'
elif sys.argv[1].lower() == 'df':
    scores_list = None
    algorithm = 'Depth First'
    algorithm_abrev = 'df'
else:
    raise AssertionError ("Geen valide naam!")


# Stel de hoogst behaalde score vast
highest_score  = max(scores_list)

# Creëer een niet-genormaliseerde histogram (density=False)
n, bins, patches = plt.hist(scores_list, bins=60, density=False, facecolor='green', alpha=0.75)

# Voeg labels en titel toe
plt.xlabel('K')
plt.ylabel('Frequency')
plt.title(f"Scores of {algorithm} Algorithm ({N} iterations):")
plt.grid(True)
bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white")
plt.text(0.65, 0.95, f"Highest score: {highest_score}", transform=plt.gca().transAxes, fontsize=11, verticalalignment='top', bbox=bbox_props)

# Sla plot op en laat de plot zien
plt.savefig(f"../../docs/{algorithm_abrev}_hist.png")
plt.show()