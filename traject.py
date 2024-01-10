class Traject:
    def __init__(self, start, eind):
        self.start = start
        self.eind = eind
        self.afstand = abs(start - eind)

if __name__ == "__main__":
    traject = Traject(1, 3)
    print(traject.afstand)





    
