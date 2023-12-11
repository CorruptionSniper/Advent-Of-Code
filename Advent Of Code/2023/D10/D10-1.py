ADJ_CONNECTIONS = {'|':[True,False,True,False],
               '-':[False,True,False,True],
               'L':[True,True,False,False],
               'J':[True,False,False,True],
               '7':[False,False,True,True],
               'F':[True,True,True,False],
               '.':[False,False,False,False],
               'S':[True,True,True,True]}
X, Y = 0, 1
ADJ = []
MAZE = []

class MazeCoord():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if 0 <= x < len(MAZE[0]) and 0 <= y < len(MAZE):
            self.symbol = MAZE[self.y][self.x]
        else:
            self.symbol = '.'

    def getAdjValid(self):
        adjValid = []
        for i, pos, isConnected in zip(range(4), ADJ, ADJ_CONNECTIONS[self.symbol]):
            adj = self + pos
            if isConnected and ADJ_CONNECTIONS[adj.symbol][(i+2)%4]:
                adjValid.append(adj)
        return adjValid
    
    def __add__(self, coord):
        return MazeCoord(self.x + coord.x, self.y - coord.y)
    
    def __eq__(self, coord):
        return self.x == coord.x and self.y == coord.y
    
    
class MazeParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getMaze(self):
        return [line[:-1] for line in self.lines[:-1]] + [self.lines[-1]]
    
    def getStartCoord(self):
        for y ,line in enumerate(self.lines):
            try:
                x = line.index('S')
                return MazeCoord(x, y)
            except ValueError:
                continue

class MazeNavigation():
    def __init__(self, coords:MazeCoord):
        self.start = coords

    def findFurthest(self):
        branches = self.start.getAdjValid()
        prev = [self.start]
        temp = []
        i = 0
        while branches:
            i += 1
            j = 0
            temp[:] = branches
            while j < len(branches):
                adjs = [x for x in branches[j].getAdjValid() if x not in prev]
                branches[j:j+1] = adjs
                j += len(adjs)
            prev[:] = temp
        return i

parser = MazeParser(r"2023\D10\D10.txt")
MAZE = parser.getMaze()
ADJ = [MazeCoord(0,1),MazeCoord(1,0),MazeCoord(0,-1),MazeCoord(-1,0)]
startCoord = parser.getStartCoord()
print(MazeNavigation(startCoord).findFurthest())