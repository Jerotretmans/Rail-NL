import sys
sys.path.append('../')
from helpers import read_csv_file
sys.path.append('../classes')
from dienstregeling import Regeling
sys.path.append('../algorithms')
from randalg import run_randalg_N_times
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from scipy.stats import norm


# Generate scores list (assuming run_randalg_N_times is defined)
scores_list = run_randalg_N_times(10000)

# Fit a normal distribution to the data
(mu, sigma) = norm.fit(scores_list)

# Create histogram without normalizing (density=False)
n, bins, patches = plt.hist(scores_list, bins=60, density=False, facecolor='green', alpha=0.75)

# Calculate bin width for scaling the normal distribution curve
bin_width = bins[1] - bins[0]

# Add a 'best fit' line using the scaled normal distribution curve
plt.plot(bins, norm.pdf(bins, mu, sigma) * len(scores_list) * bin_width, 'r--', linewidth=2)

# Add labels and title
plt.xlabel('K')
plt.ylabel('Frequency')
plt.title(r'$\mathrm{Histogram\ of\ scores:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
plt.grid(True)

plt.show()