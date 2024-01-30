import sys
sys.path.append('/classes')

import random

from classes.traject import Traject
from classes.dienstregeling import Regeling

def run_hill_climber(algorithm_instance, regio):
    
    # Initialiseer een toestand van de dienstregeling
    state = Regeling()
    traject = Traject()

    # Stel maxima in op basis van de regio
    if regio == 'h':
        state.max_trajecten = 7
        traject.max_tijd = 120
    elif regio == 'nl':
        state.max_trajecten = 20
        traject.max_tijd = 180
    else:
        raise AssertionError ("Geen valide naam!")