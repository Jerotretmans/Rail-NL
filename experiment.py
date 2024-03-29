import sys
sys.path.append('code')
sys.path.append('code/visualisation')

import statistics

from code.helpers import read_csv_file, load_algorithms_dict
from code.classes.algorithm import Algorithm
from code.visualisation.hist import make_histogram


"""
Experiment script.

Gebruik de README.md als gebruiksaanwijzing!
"""


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
        alg_object1 = Algorithm('bizzey', stations_data, connections_data)
        alg_object1.create_station_objects()
        alg_object2 = Algorithm('rustaaahg', stations_data, connections_data)
        alg_object2.create_station_objects()

        # Definieer de scores voor de twee cases van experiment 1
        results1 = alg_object1.run_algorithm_for_60_sec(alg_object1, aantal_trajecten=None)
        states1 = [result[0] for result in results1]
        scores1 = [result[1] for result in results1]
        high_score1 = max(scores1)
        print(f"Highest score: {high_score1}")

        results2 = alg_object1.run_algorithm_for_60_sec(alg_object1, aantal_trajecten=None)
        states2 = [result[0] for result in results2]
        scores2 = [result[1] for result in results2]
        high_score2 = max(scores2)
        print(f"Highest score: {high_score2}")

        # Plot een histogram
        if histogram == 'y':
            make_histogram(scores1, len(scores1), 'br')
            make_histogram(scores2, len(scores2), 'qr')
        else:
            pass

    elif sys.argv[1].lower() == 'exp2':
        
        # Vraagt de gebruiker welk algoritme hij/zij wilt gebruiken voor het experiment
        alg_name = None
        while alg_name == None:
            alg_afk = str(input("Voor welk algoritme wil je het experiment uitvoeren?\n {gr, hc, sa, df, bf}: ")).lower()

            # Runt desbetreffende algoritme 
            if alg_afk.lower() in alg_dict:
                alg_name: str = alg_dict[alg_afk.lower()]
            else:
                print("Geen valide algoritme!")

        aantal_trajecten = 0
        while aantal_trajecten < 1 or aantal_trajecten > 7:
            aantal_trajecten = int(input("Hoeveel trajecten wil je instellen? (1 - 7): "))

        # Creeërt een algoritme object voor aangegeven hoeveelheid trajecten
        alg_object = Algorithm(alg_name, stations_data, connections_data)
        alg_object.create_station_objects()
        
        # Runt algoritme voor 60 sec en creërt een lijst met alle gecreërde states met scores
        results = alg_object.run_algorithm_for_60_sec(alg_object, aantal_trajecten)
        states = [result[0] for result in results]
        scores = [result[1] for result in results]

        # Verkrijgt de index voor de hooste score in de score lijst
        index_highest_score = scores.index(max(scores))
        # Slaat de beste state op
        best_state = states[index_highest_score]
    
        high_score: int = max(scores)
        average_score = statistics.mean(scores)
        print(best_state)
        print(f"Highest score: {high_score}")
        print(f"average score: {average_score}")

    else:
        print("Geen experiment met die naam gevonden!")
