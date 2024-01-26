import sys
sys.path.append('../')
sys.path.append('../classes')
sys.path.append('../algorithms')

from helpers import read_csv_file

from dienstregeling import Regeling

from randalg import run_randalg_N_times
# from randalg2 import run_alg_N_times

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm


"""
Maakt een histogram van de scores van verschillende algoritmes.  

Usage: 'python3 hist.py (algorithm)' where (algorithm) is one of the following abbreviations:

rd for random
gr for greedy
hc for hill climber

Example: 'python3 hist.py rd' 
"""

# Verzeker het correcte gebruik van de code
assert len(sys.argv) == 2, """Usage: 'python3 hist.py (algorithm)' "
where (algorithm) is on of the following abbreviations:

rd for random
gr for greedy
hc for hill climber

Example: 'python3 hist.py rd'
"""

try:
    # Ask the user for input
    N = int(input("How many times do you want to run the algorithm? "))
# Only accept integers
except ValueError:
    print("Please enter a valid integer.")

if sys.argv[1].lower() == 'rd':
    scores_list = run_randalg_N_times(N)
    algorithm = 'Random'
    algorithm_abrev = 'rd'
elif sys.argv[1].lower() == 'gr':
    # scores_list = run_alg_N_times(1000)
    algorithm = 'Greedy'
    algorithm_abrev = 'gr'
elif sys.argv[1] == 'hc':
    # scores_list = run_alg_N_times(1000)
    algorithm = 'Hill Climber'
    algorithm_abrev = 'hc'
else:
    raise AssertionError ("Geen valide naam!")


# Creëer een niet-genormaliseerde histogram (density=False)
n, bins, patches = plt.hist(scores_list, bins=60, density=False, facecolor='green', alpha=0.75)

# Voeg labels en titel toe
plt.xlabel('K')
plt.ylabel('Frequency')
# plt.title(r'$\mathrm{Histogram\ of\ scores:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
plt.title(f"Scores of {algorithm} Algorithm:")
plt.grid(True)
bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white")
plt.text(0.7, 0.95, f"{N} iterations", transform=plt.gca().transAxes, fontsize=11, verticalalignment='top', bbox=bbox_props)

plt.savefig(f"../../docs/{algorithm_abrev}_hist.png")
plt.show()