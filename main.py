import sys
sys.path.append('code')
sys.path.append('code/algorithms')
sys.path.append('data')

from code.helpers import read_csv_file

from code.algorithms.randalg import run_randalg
from code.algorithms.depth_first import run_depth_first
# from code.algorithms.breadth_first import run_breadth_first
# from hill_climber import run_hc_N_times

from code.classes.algorithm import Algorithm
from code.classes.stations import Station

if __name__ == "__main__":

    # Verzeker het correcte gebruik van de code
    assert len(sys.argv) == 2, "Usage: 'python3 main.py holland' or 'python3 main.py nl'"

    # Data lezen
    if sys.argv[1].lower() == 'holland':
        stations_data = read_csv_file('data/StationsHolland.csv')
        connections_data = read_csv_file('data/ConnectiesHolland.csv')
    elif sys.argv[1].lower() == 'nl':
        stations_data = read_csv_file('data/StationsNationaal.csv')
        connections_data = read_csv_file('data/ConnectiesNationaal.csv')
    else:
        raise AssertionError ("Usage: 'python3 bokehmap.py holland' or 'python3 bokehmap.py nl'")

    
    randalg_object = Algorithm('random', stations_data, connections_data)

    randalg_object.create_station_objects()

    randalg_object.run_algorithm(randalg_object)

    # Vraag om een hoeveelheid runs van het algoritme
    try:
        N = int(input("Hoe vaak moet het algoritme worden uitgevoerd "))
    # Accepteer alleen integers
    except ValueError:
        print("Alleen hele getallen a.u.b.")

    # Run het algoritme hoe vaak de gebruiker opgeeft
    scores = randalg_object.run_algorithm_N_times(N)
    high_score = max(scores)
    print(f"Highest score: {high_score}")