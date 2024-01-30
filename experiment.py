import sys
sys.path.append('code')
sys.path.append('code/visualisation')

from code.helpers import read_csv_file, load_algorithms_dict

from code.classes.algorithm import Algorithm

from code.visualisation.hist import make_histogram


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
        alg_object = Algorithm('simulated annealing', stations_data, connections_data, max_trajecten_holland, max_tijd_traject_holland, alle_connecties_holland)
        alg_object.run_algorithm(alg_object, regio)

    else:
        print("Geen experiment met die naam gevonden!")
