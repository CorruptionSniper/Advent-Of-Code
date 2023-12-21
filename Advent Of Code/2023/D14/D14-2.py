EMPTY, MOVABLE, FIXED = '.', 'O', '#'
NORTH, WEST, SOUTH, EAST = (0,-1), (-1,0), (0,1), (1,0)
CYCLE = [NORTH, WEST, SOUTH, EAST]
X, Y = 0, 1

class TerrainMapParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getTerrain(self):
        return [list(line.strip('\n')) for line in self.lines]

class Terraformer():
    def __init__(self, terrain):
        self.terrain = terrain

    def terraform(self, direction):
        if direction[1]:
            self.__yterraform(direction[1])
        else:
            self.__xterraform(direction[0])
    

    def __xterraform(self, direction):
        c = 0 if direction == 1 else -1
        for row in self.terrain:
            movableN = 0
            for y in range(c,len(terrain)*direction+c,direction):
                symbol = row[y]
                if symbol == MOVABLE:
                    row[y] = EMPTY
                    movableN += 1
                elif movableN and symbol == FIXED:
                    y -= direction
                    row[y-(movableN-1)*(c+1):y-movableN*c+c+1] = [MOVABLE for i in range(movableN)]
                    movableN = 0
            row[y-(movableN-1)*(c+1):y-movableN*c+c+1] = [MOVABLE for i in range(movableN)]

    def __yterraform(self, direction):
        c = 0 if direction == 1 else -1
        for cI in range(len(self.terrain)):
            movableN = 0
            for x in range(c,len(terrain)*direction+c,direction):
                symbol = self.terrain[x][cI]
                if symbol == MOVABLE:
                    self.terrain[x][cI] = EMPTY
                    movableN += 1
                elif movableN and symbol == FIXED:
                    x -= direction
                    for i in range(x-(movableN-1)*(c+1),x-movableN*c+c+1):
                        self.terrain[i][cI] = MOVABLE
                    movableN = 0
            for i in range(x-(movableN-1)*(c+1),x-movableN*c+c+1):
                self.terrain[i][cI] = MOVABLE

class TerrainLoadAnalyser():
    def __init__(self, terrain):
        self.terrain = terrain
        self.Terraformer = Terraformer(self.terrain)

    def getCycle(self, cycles):
        prevTerrains = []
        while self.cycle() not in prevTerrains:
            prevTerrains.append([x.copy() for x in self.terrain])
        s = prevTerrains.index(self.terrain)
        if cycles - 1 < s:
            return prevTerrains[cycles - 1]
        #print(s, period, cycles)
        #print([TerrainLoadAnalyser.calculateLoad(x) for x in prevTerrains[-period:]])
        return prevTerrains[s + ((cycles - s - 1) % (len(prevTerrains) - s))]

    def cycle(self):
        for direction in CYCLE:
            self.Terraformer.terraform(direction)
        return self.terrain

    @staticmethod
    def calculateLoad(terrainAtCycle):
        rSum = 0
        for i, row in enumerate(terrainAtCycle[::-1],1):
            rSum += row.count(MOVABLE)*i
        return rSum

nCycles = 1000000000
terrain = TerrainMapParser(r"2023\D14\D14.txt").getTerrain()
analyser = TerrainLoadAnalyser(terrain)
print(TerrainLoadAnalyser.calculateLoad(analyser.getCycle(nCycles)))