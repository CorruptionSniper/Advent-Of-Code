X, Y = 0, 1
ROWS, COLUMNS = 0, 1
GALAXY = '#'
class CosmosParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()
    
    def getGalaxies(self):
        galaxies = []
        for y, line in enumerate(self.lines):
            for x, char in enumerate(line):
                if char == GALAXY:
                    galaxies.append([x,y])
        return galaxies

class CosmosCalculator():
    def __init__(self, galaxies, cosmosSize):
        self.galaxies = galaxies
        self.cosmosSize = cosmosSize

    def getGalaxiesCategorised(self):
        rows = [[] for x in range(self.cosmosSize[Y])]
        columns = [[] for x in range(self.cosmosSize[X])]
        i = 0
        for galaxy in self.galaxies:
            rows[galaxy[Y]].append(galaxy)
            columns[galaxy[X]].append(galaxy)
        return [rows, columns]

    def normalise(self):
        cGalaxies = self.getGalaxiesCategorised()
        i = 0
        for row in cGalaxies[ROWS]:
            if len(row):
                for galaxy in row:
                    galaxy[Y] += i
            else:
                i += 1
        i = 0
        for column in cGalaxies[COLUMNS]:
            if len(column):
                for galaxy in column:
                    galaxy[X] += i
            else:
                i += 1
        self.galaxies = []
        for row in cGalaxies[ROWS]:
            for galaxy in row:
                self.galaxies.append(galaxy)
    
    @staticmethod
    def getDistance(g1, g2):
        return abs(g1[Y]-g2[Y]) + abs(g1[X]-g2[X])
    
    def totalDistances(self):
        self.normalise()
        totalDistance = 0
        for i in range(len(self.galaxies)-1):
            for j in range(i+1,len(self.galaxies)):
                totalDistance += self.getDistance(self.galaxies[i], self.galaxies[j])
        return totalDistance

parser = CosmosParser(r"2023\D11\D11.txt")
galaxies = parser.getGalaxies()
print(CosmosCalculator(galaxies, (len(parser.lines),len(parser.lines[0]))).totalDistances())