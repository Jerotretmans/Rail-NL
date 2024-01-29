import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from helpers import load_algorithms_dict


"""
Maakt een histogram van de scores van verschillende algoritmes.
"""

alg_dict = load_algorithms_dict()

def make_histogram(scores_list, N, alg_abrev):

    # Stel de hoogst behaalde score vast
    highest_score  = max(scores_list)

    # Creëer een niet-genormaliseerde histogram (density=False)
    plt.hist(scores_list, bins=60, density=False, facecolor='green', alpha=0.75)

    # Voeg labels en titel toe
    plt.xlabel('K')
    plt.ylabel('Frequency')
    plt.title(f"Scores of {alg_dict[alg_abrev]} Algorithm ({N} iterations):")
    plt.grid(True)
    bbox_props = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white")
    plt.text(0.65, 0.95, f"Highest score: {highest_score}", transform=plt.gca().transAxes, fontsize=11, verticalalignment='top', bbox=bbox_props)

    # Laat de plot zien en sla het op
    plt.show()
    plt.savefig(f"docs/{alg_abrev}_hist.png")
