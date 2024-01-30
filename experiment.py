import sys
sys.path.append('code')
sys.path.append('code/visualisation')

import subprocess
import time

from code.helpers import read_csv_file, load_algorithms_dict, export_output

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
    if sys.argv[1].lower() in alg_dict:
        alg_name = alg_dict[sys.argv[1].lower()]

        alg_object = Algorithm(alg_name, stations_data, connections_data)
        alg_object.create_station_objects()   

    elif sys.argv[1].lower() == 'exp2':
        alg_object = Algorithm('Simulated Annealing', stations_data, connections_data)

    else:
        print("Geen experiment met die naam gevonden!")
    

    # Run algoritme op verzoek van de gebruiker
    if sys.argv[2].lower() in alg_dict:
        alg_name = alg_dict[sys.argv[2].lower()]

        alg_object = Algorithm(alg_name, stations_data, connections_data)
        alg_object.create_station_objects()
    else:
        print("Geen valide naam!")

    start = time.time()
    N = 0

    while time.time() - start < 3600:
        print(f"run: {N}")
        subprocess.call(["timeout", "60", "python3", "random_algorithm.py"])
        N += 1

    # Vraag of de gebruiker een histogram wilt zien van de scores
    histogram = 'y'

    # Run het algoritme hoe vaak de gebruiker opgeeft
    results = alg_object.run_algorithm_N_times(N, alg_object)
    best_state: object = results[0]
    scores_list = results[1]
    print(scores_list)
    high_score = max(scores_list)
    print(f"Highest score: {high_score}")

    
    # Plot een histogram als de gebruiker dat opgeeft
    if histogram == 'y':
        make_histogram(scores_list, N, sys.argv[1].lower())
    elif histogram == 'n':
        pass
