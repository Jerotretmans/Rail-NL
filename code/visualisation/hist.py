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

scores_list = run_randalg_N_times()

plt.xlim(0, 10000)
plt.hist(scores_list, bins = 20)
plt.show()