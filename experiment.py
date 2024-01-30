import sys
sys.path.append('code')
sys.path.append('code/visualisation')

import subprocess
import time

from code.helpers import read_csv_file, load_algorithms_dict

from code.classes.algorithm import Algorithm

from code.visualisation.hist import make_histogram


"""
Experiment script.

Gebruik de README.md als gebruiksaanwijzing!
"""



if __name__ == "__main__":

    # Verzeker het correcte gebruik van de code
    assert len(sys.argv) == 2 or len(sys.argv) == 3, "Error: Gebruik de README.md als gebruiksaanwijzing!"

    # Laad de namen van de algoritmes vanuit helpers
    alg_dict = load_algorithms_dict()

    # Stel regio in
    regio = 'h'

    # Lees de data voor de desbetreffende regio
    if regio == 'h':
        stations_data = read_csv_file('data/StationsHolland.csv')
        connections_data = read_csv_file('data/ConnectiesHolland.csv')


    # Run het experiment dat de gebruiker aangeeft
    if sys.argv[1].lower() == 'exp1':
        alg_object1 = Algorithm('bizzey', stations_data, connections_data)
        alg_object1.create_station_objects()
        alg_object2 = Algorithm('rustaaahg', stations_data, connections_data)
        alg_object2.create_station_objects()

    elif sys.argv[1].lower() == 'exp2':
        alg_object = Algorithm('Simulated Annealing', stations_data, connections_data)

    else:
        print("Geen experiment met die naam gevonden!")
    

    start = time.time()
    N = 0

    while time.time() - start < 3600:
        print(f"run: {N}")
        subprocess.call(["timeout", "60", "python3", "random_algorithm.py"])
        N += 1

    # Vraag of de gebruiker een histogram wilt zien van de scores
    histogram = 'y'


    results1 = alg_object.run_algorithm_N_times(N, alg_object1)
    best_state1: object = results1[0]
    scores_list1 = results1[1]
    high_score = max(scores_list1)
    print(f"Highest score: {high_score}")

    results2 = alg_object.run_algorithm_N_times(N, alg_object2)
    best_state2: object = results2[0]
    scores_list2 = results2[1]
    high_score = max(scores_list2)
    print(f"Highest score: {high_score}")

    
    # Plot een histogram als de gebruiker dat opgeeft
    if histogram == 'y':
        make_histogram(scores_list1, N, sys.argv[1].lower())
        make_histogram(scores_list1, N, sys.argv[1].lower())
    elif histogram == 'n':
        pass
