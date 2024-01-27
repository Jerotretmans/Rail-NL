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

    # Gebruik random algoritme --> Werkt
    # randalg_object = Algorithm('random', stations_data, connections_data)
    # randalg_object.create_station_objects()
    # alg_object = randalg_object

    # Gebruik greedy algoritme --> Werkt
    # greedy_object = Algorithm('greedy', stations_data, connections_data)
    # greedy_object.create_station_objects()
    # alg_object = greedy_object

    # Gebruik depth_first algoritme --> Werkt
    # depth_first_object = Algorithm('depth first', stations_data, connections_data)
    # depth_first_object.create_station_objects()
    # alg_object = depth_first_object

    # Gebruik breath_first algoritme
    breath_first_object = Algorithm('breath first', stations_data, connections_data)
    breath_first_object.create_station_objects()
    alg_object = breath_first_object


    # Vraag om een hoeveelheid runs van het algoritme
    try:
        N = int(input("Hoe vaak moet het algoritme worden uitgevoerd "))
    # Accepteer alleen integers
    except ValueError:
        print("Alleen hele getallen a.u.b.")

    # Run het algoritme hoe vaak de gebruiker opgeeft
    scores = alg_object.run_algorithm_N_times(N, alg_object)
    print(scores)
    high_score = max(scores)
    print(f"Highest score: {high_score}")
