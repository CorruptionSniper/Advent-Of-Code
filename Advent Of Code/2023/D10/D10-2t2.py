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
    
    def getAdj(self):
        adjs = []
        for i in range(-1,2):
            for j in range(-1,2):
                if i or j:
                    adj = self + MazeCoord(i, j)
                    if 0 <= adj.x < len(MAZE[0]) and 0 <= adj.y < len(MAZE):
                        adjs.append(adj)
        return adjs
    
    def __add__(self, coord):
        return MazeCoord(self.x + coord.x, self.y - coord.y)
    
    def __eq__(self, coord):
        return self.x == coord.x and self.y == coord.y
    
    def getCoords(self):
        return self.x, self.y
    
    
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

"""def binarySearch(array, element, mid=0):
    lb = 0
    ub = len(array) - 1
    while lb < ub:

    return mid"""

class MazeNavigation():
    def __init__(self, coords:MazeCoord):
        self.start = coords

    def getMazeTrace(self):
        visited = [[False]*len(MAZE[0]) for y in range(len(MAZE))]
        branches = self.start.getAdjValid()
        prev = [self.start]
        temp = []
        visited[self.start.y][self.start.x] = True
        while branches:
            for branch in branches:
                visited[branch.y][branch.x] = True
            j = 0
            temp[:] = branches
            while j < len(branches):
                adjs = [x for x in branches[j].getAdjValid() if x not in prev]
                branches[j:j+1] = adjs
                j += len(adjs)
            prev[:] = temp
        return visited
    
    def floodFillOutside(self):
        visited = self.getMazeTrace()
        height = len(MAZE) - 1
        width = len(MAZE[0]) - 1
        #INITIAL BRANCHES = MAZE RIM (but not maze perimeter)
        branches = [MazeCoord(i,0) for i in range(width+1) if not visited[0][i]] #TOP RIM
        branches += [MazeCoord(0,i) for i in range(1,height) if not visited[i][0]] #LEFT RIM
        branches += [MazeCoord(width,i) for i in range(1,height) if not visited[i][width]] #RIGHT RIM
        branches += [MazeCoord(i,height) for i in range(width+1) if not visited[height][i]] #BOTTOM RIM
        while branches:
            for branch in branches:
                visited[branch.y][branch.x] = True
            j = 0
            while j < len(branches):
                adjs = [b for b in branches[j].getAdj() if not visited[b.y][b.x]]
                branches[j:j+1] = adjs
                j += len(adjs)
        return visited 

parser = MazeParser(r"2023\D10\D10 test4A.txt")
MAZE = parser.getMaze()
ADJ = [MazeCoord(0,1),MazeCoord(1,0),MazeCoord(0,-1),MazeCoord(-1,0)]
startCoord = parser.getStartCoord()
matrix = MazeNavigation(startCoord).floodFillOutside()
print("\n".join(["".join(["1" if l else "0" for l in row]) for row in matrix]))
print(sum([row.count(False) for row in matrix]))