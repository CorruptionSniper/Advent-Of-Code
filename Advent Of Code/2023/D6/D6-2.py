from math import sqrt, ceil, floor
T, S = 0, 1
INFINITESIMAL = 2**-47

class RaceInfoParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getRaceInfo(self):
        times = int(self.lines[T][9:].replace(" ",""))
        distance = int(self.lines[S][9:].replace(" ",""))
        return [(times, distance)]

def getSolutions(a, b, c):
    discriminant = sqrt((b**2)-4*a*c)
    offset = -b
    denominator = 2*a 
    return (offset - discriminant)/denominator, (offset + discriminant)/denominator

class RaceMargins():
    def __init__(self, races):
        self.races = races

    def getRaceMargins(self):
        product = 1
        for race in self.races:
            product *= self.getWaysToWin(race)
        return product
    
    """
    Distance travelled = timeHeld*(totalTime-timeHeld); 
    s = t(T-t)
    T^2 - Tt + s = 0
    TimeHeld solutions; t = (T ± sqrt(T^2 - 4*s))/2
    The solutions are the interval in which timeHeld is just enough to beat the race, 
    therefore the range of values is the total number of ways to win.
    WaysToWin = solution2-solution1:
    """
    def getWaysToWin(self, race):
        solutions = getSolutions(1, -race[T], race[S])
        return floor(solutions[1] - INFINITESIMAL) - ceil(solutions[0] + INFINITESIMAL) + 1

races = RaceInfoParser(r"Advent Of Code\2023\D6\D6.txt").getRaceInfo()
print(RaceMargins(races).getRaceMargins())