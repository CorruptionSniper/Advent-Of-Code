L, R = 0, 1
class MapParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getDirections(self):
        return [L if x == 'L' else R for x in self.lines[0]]
    
    def getMap(self):
        parsedLines = [line.split(' = ') for line in self.lines[2:]]
        desertMap = {line[0]:line[1].strip('()\n').split(', ') for line in parsedLines}
        return desertMap

class Navigator():
    def __init__(self, desertMap, directions):
        self.directions = directions
        self.map = desertMap

    def getSteps(self, pointer, end):
        i = 0
        mod = len(self.directions) - 1
        while pointer != end:
            pointer = self.map[pointer][self.directions[i % mod]]
            i += 1
        return i

parser = MapParser(r"2023\D8\D8.txt")
directions = parser.getDirections()
desertMap = parser.getMap()
print(Navigator(desertMap, directions).getSteps("AAA", "ZZZ"))