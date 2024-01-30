import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

from helpers import load_algorithms_dict


"""
Maakt een grafiekje van de scores van een algoritme in chronologische volgorde.
"""

alg_dict = load_algorithms_dict()

def plot_scores(scores_list, N):

    # Stel de hoogst behaalde score vast
    highest_score  = max(scores_list)

    plt.plot(scores_list, color='red')

    # Voeg labels en titel toe
    plt.xlabel('Iterations')
    plt.ylabel('K')
    plt.title(f"Scores of Simulated Annealing Algorithm ({N} iterations):")
    plt.text(0.65, 0.95, f"Highest score: {highest_score}", fontsize=11)

    # Laat de plot zien en sla het op
    plt.savefig(f"docs/sim_ann_plot.png")
    plt.show()
    
