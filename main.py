import sys
sys.path.append('code')
sys.path.append('code/visualisation')

from code.helpers import read_csv_file, load_algorithms_dict
from code.classes.algorithm import Algorithm
from code.visualisation.hist import make_histogram


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

    elif regio == 'nl':
        stations_data = read_csv_file('data/StationsNationaal.csv')
        connections_data = read_csv_file('data/ConnectiesNationaal.csv')

    T = None

    # Run algoritme op verzoek van de gebruiker
    if sys.argv[1].lower() in alg_dict:
        alg_afk = sys.argv[1].lower()
        alg_name = alg_dict[alg_afk]

        alg_object = Algorithm(alg_name, stations_data, connections_data)
        alg_object.create_station_objects()

        if alg_afk == 'gr' or alg_afk == 'hc' or alg_afk == 'sa':
            while T == None:
                T = int(input("Hoeveel trajecten moeten er worden gemaakt? ")) 

    else:
        print("Geen valide naam!")

    while True:
        # Vraag om een hoeveelheid runs van het algoritme
        try:
            N = int(input("Hoe vaak moet het algoritme worden uitgevoerd? "))
            if N <= 0:
                print("Alleen gehele getallen boven 0 zijn toegestaan.")
            else:
                break
        except ValueError:
            print("Alleen gehele getallen a.u.b.")

    # Vraag of de gebruiker een histogram wilt zien van de scores
    histogram = None
    while histogram not in ['y', 'n']:
        histogram = str(input("Wil je een histogram van de data? (y/n): ")).lower()

        if histogram not in ['y', 'n']:
            print("Ongeldige invoer. Type 'y' voor wel een histogram of 'n' voor geen histogram.")

    
    # Run het algoritme hoe vaak de gebruiker heeft opgegeven
    results = alg_object.run_algorithm_N_times(N, alg_object, regio, T)

    # Return states en scores van de runs
    states = [result[0] for result in results]
    scores = [result[1] for result in results]

    # Bepaal de hoogste score die behaald is
    high_score = max(scores)
    print(f"Highest score: {high_score}")

    
    # Plot een histogram als de gebruiker dat heeft opgegeven
    if histogram == 'y':
        make_histogram(scores, N, sys.argv[1].lower())
    elif histogram == 'n':
        pass
