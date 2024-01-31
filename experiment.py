import sys

from typing import List, Dict, Optional
import statistics
sys.path.append('code')
sys.path.append('code/algorithms')
sys.path.append('data')

from code.helpers import read_csv_file, load_algorithms_dict

from code.classes.algorithm import Algorithm

"""
Experiment script.

Gebruik de README.md als gebruiksaanwijzing!
"""


max_trajecten_holland = 7
max_tijd_traject_holland = 120
alle_connecties_holland = 28


if __name__ == "__main__":

    # Verzeker het correcte gebruik van de code
    assert len(sys.argv) == 2, "Error: Gebruik de README.md als gebruiksaanwijzing!"

    # Laad de namen van de algoritmes vanuit helpers
    alg_dict = load_algorithms_dict()

    # Stel regio in
    regio = 'h'

    # Lees de data voor de desbetreffende regio
    if regio == 'h':
        stations_data = read_csv_file('data/StationsHolland.csv')
        connections_data = read_csv_file('data/ConnectiesHolland.csv')

    # Laat altijd een histogram zien
    histogram = 'y'

    # Run het experiment dat de gebruiker aangeeft
    if sys.argv[1].lower() == 'exp1':
        alg_object1 = Algorithm('bizzey', stations_data, connections_data, max_trajecten_holland, max_tijd_traject_holland, alle_connecties_holland)
        alg_object1.create_station_objects()
        alg_object2 = Algorithm('rustaaahg', stations_data, connections_data, max_trajecten_holland, max_tijd_traject_holland, alle_connecties_holland)
        alg_object2.create_station_objects()

        # Definieer de scores voor de twee cases van experiment 1
        scores_list1 = alg_object1.run_algorithm_for_60_sec(alg_object1)
        high_score = max(scores_list1)
        print(f"Highest score: {high_score}")

        scores_list2 = alg_object2.run_algorithm_for_60_sec(alg_object2)
        high_score = max(scores_list2)
        print(f"Highest score: {high_score}")

        # Plot een histogram
        if histogram == 'y':
            make_histogram(scores_list1, len(scores_list1), 'br')
            make_histogram(scores_list2, len(scores_list2), 'qr')
        else:
            pass

    elif sys.argv[1].lower() == 'exp2':
        alg_object = Algorithm('Simulated Annealing', stations_data, connections_data, max_trajecten_holland, max_tijd_traject_holland, alle_connecties_holland)


    elif sys.argv[1].lower() == 'exp3':
        # random niet mogelijk want random
        alg_name = None
        while alg_name == None:
            alg_afk = str(input("Voor welk algoritme wil je het experiment uitvoeren? <gr, hc, sa, df, bf>: ")).lower()
        # Run algoritme op verzoek van de gebruiker
            if alg_afk.lower() in alg_dict:
                alg_name: str = alg_dict[alg_afk.lower()]
            else:
                print("Geen valide algoritme!")
        aantal_trajecten = 0
        while aantal_trajecten < 1 or aantal_trajecten > 7:
            aantal_trajecten = int(input("Hoeveel trajecten wil je instellen? (1 - 7): "))

        alg_object: Algorithm = Algorithm(alg_name, stations_data, connections_data, aantal_trajecten, max_tijd_traject_holland, alle_connecties_holland)
        alg_object.create_station_objects()

        results = alg_object.run_algorithm_for_60_sec(alg_object)
        states = [result[0] for result in results]
        scores = [result[1] for result in results]
        print(scores)
        index_highest_score = scores.index(max(scores))
        # print(index_highest_score)
        best_state = states[index_highest_score]
        print(best_state)
        # als je experiment wilt runnen
        high_score: int = max(scores)
        average_score = statistics.mean(scores)
        print(f"Highest score: {high_score}")
        print(f"average score: {average_score}")
        
    else:
        print("Geen valide naam!")
        

        
