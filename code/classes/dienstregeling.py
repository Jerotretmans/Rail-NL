from stations import Station
from traject import Traject
import sys
sys.path.append('../')
from helpers import read_csv_file

class Regeling:
    """
    Een verzameling trajecten die samen zo veel mogelijk stations bereikt in zo min 
    mogelijk tijd. Score: K = p*10000 - (T*100 + Min)
    
    Constraint: max 7 trajecten
    """
    def __init__(self, name) -> None:
        pass

    def a


if __name__ == "__main__":

    connections = read_csv_file('../../data/ConnectiesHolland.csv')
    # print(connections)
    
    
