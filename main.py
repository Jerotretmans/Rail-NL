import sys
sys.path.append('code')
sys.path.append('code/visualisation')

from code.helpers import read_csv_file, load_algorithms_dict, export_output

from code.classes.algorithm import Algorithm

from code.visualisation.hist import make_histogram
from code.visualisation.plot import plot_scores


"""
Main functie voor het runnen van de geïmplementeerde algoritmes voor case RailNL.
Vak: Algoritmen en Heuristieken, ter afsluiting van de Minor Programmeren.

"Spoorjewel":
    Menno Rooker
    Ron Lakeman
    Jero Tretmans

Januari 2024


Gebruik de README.md als gebruiksaanwijzing!
"""

# maximaal antaal trajecten en tijd per traject gebasseerd op regio
max_trajecten_holland = 7
max_trajecten_nationaal = 20
max_tijd_traject_holland = 120
max_tijd_traject_nationaal = 180
alle_connecties_holland = 28
alle_connecties_nationaal = 89 

if __name__ == "__main__":

    # Verzeker het correcte gebruik van de code
    assert len(sys.argv) == 2 or len(sys.argv) == 3, "Error: Gebruik de README.md als gebruiksaanwijzing!"

    # Laad de namen van de algoritmes vanuit helpers
    alg_dict = load_algorithms_dict()

    # Vraag aan de gebruiker voor welke regio het algoritme moet worden uitgevoerd
    regio = None
    while regio not in ['h', 'nl']:
        regio = str(input("Voor regio Holland of Nationaal? (h/nl): ")).lower()

        if regio not in ['h', 'nl']:
            print("Ongeldige invoer. Type 'h' voor Holland of 'nl' voor Nationaal.")

    # Lees de data voor de desbetreffende regio
    if regio == 'h':
        stations_data = read_csv_file('data/StationsHolland.csv')
        connections_data = read_csv_file('data/ConnectiesHolland.csv')
        max_trajecten = max_trajecten_holland
        max_tijd_traject = max_tijd_traject_holland
        alle_connecties = alle_connecties_holland

    elif regio == 'nl':
        stations_data = read_csv_file('data/StationsNationaal.csv')
        connections_data = read_csv_file('data/ConnectiesNationaal.csv')
        max_trajecten = max_trajecten_nationaal
        max_tijd_traject = max_tijd_traject_nationaal
        alle_connecties = alle_connecties_nationaal

    # Run algoritme op verzoek van de gebruiker
    if sys.argv[1].lower() in alg_dict:
        alg_name = alg_dict[sys.argv[1].lower()]

        alg_object = Algorithm(alg_name, stations_data, connections_data, max_trajecten, max_tijd_traject, alle_connecties)
        alg_object.create_station_objects()
    else:
        print("Geen valide naam!")


    # Vraag om een hoeveelheid runs van het algoritme
    try:
        N = int(input("Hoe vaak moet het algoritme worden uitgevoerd "))
    # Accepteer alleen integers
    except ValueError:
        print("Alleen hele getallen a.u.b.")

    # Vraag of de gebruiker een histogram wilt zien van de scores
    histogram = None
    while histogram not in ['y', 'n']:
        histogram = str(input("Wil je een histogram van de data? (y/n): ")).lower()

        if histogram not in ['y', 'n']:
            print("Ongeldige invoer. Type 'y' voor wel een histogram of 'n' voor geen histogram.")


    # Run het algoritme hoe vaak de gebruiker opgeeft
    results = alg_object.run_algorithm_N_times(N, alg_object, regio)
    best_state: object = results[0]
    scores_list = results[1]
    high_score = max(scores_list)
    # print(best_state.traject_list)
    print(f"Highest score: {high_score}")

    
    # Plot een histogram als de gebruiker dat opgeeft
    if histogram == 'y':
        make_histogram(scores_list, N, sys.argv[1].lower())
    elif histogram == 'n':
        pass

    if len(sys.argv) == 3:
        if sys.argv[2] == 'f':
            export_output()
        else:
            pass

