EMPTY, MOVABLE, FIXED = '.', 'O', '#'

class TerrainMapParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getTerrain(self):
        return [line.strip('\n') for line in self.lines]
    
class TerrainLoadAnalyser():
    def __init__(self, terrain):
        self.terrain = terrain

    def calculateLoad(self):
        return sum([self.calculateColumnLoad(i) for i in range(len(self.terrain[0]))])
    
    def calculateColumnLoad(self, cI):
        columnSum = 0
        movableN = 0
        for i in range(1,len(self.terrain)+1):
            symbol = self.terrain[-i][cI]
            if symbol == MOVABLE:
                movableN += 1
            elif movableN and symbol == FIXED:
                columnSum += self.localLoad(i,movableN)
                movableN = 0
        return columnSum + self.localLoad(len(self.terrain)+1,movableN)
    
    def localLoad(self, start, n):
        return ((2*start-n-1)*n)>>1
    
parser = TerrainMapParser(r"2023\D14\D14.txt")
terrain = parser.getTerrain()
print(TerrainLoadAnalyser(terrain).calculateLoad())