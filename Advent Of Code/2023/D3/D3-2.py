DIGITS = ['0','1','2','3','4','5','6','7','8','9']
BASE_SYMBOL = '.'
GEAR = '*'
NUM = 0
POS = 1
class EngineSchematicParser():
    def __init__(self, filename=None):
        if filename:
            f = open(filename)
            self.lines = f.readlines()
            f.close()
    
    def getElements(self):
        numbers = [[] for x in range(len(self.lines))]
        gears = [[] for x in range(len(self.lines))]
        for row, line in enumerate(self.lines):
            n, i, j = self.getNumber(line, 0)
            while j != len(line):
                numbers[row].append((n, (i, j)))
                n, i, j = self.getNumber(line, j + 1)
            gears[row] = self.getGears(line)
        return numbers, gears
    
    def getNumber(self, line, i):
        while i != len(line) and line[i] not in DIGITS:
            i += 1
        if i != len(line):
            j = i + 1
            while j != len(line) and line[j] in DIGITS:
                j += 1
            return int(line[i:j]), i, j - 1
        return None, None, len(line)
    
    def getGears(self, line):
        gears = []
        i = 0
        while i != len(line) - 2:
            if line[i] == '*':
                gears.append([i,[]])
            i += 1
        return gears

class EnginePartGetter():
    def __init__(self, numbers, gears):
        self.numbers = numbers
        self.gears = gears

    def getGearRatio(self):
        self.getGearAdjecent()
        gearRatio = 0
        for row in self.gears:
            for pos, adjecent in row:
                if len(adjecent) == 2:
                    gearRatio += adjecent[0] * adjecent[1]
        return gearRatio
        
    def getGearAdjecent(self):
        for i, rowNums in enumerate(self.numbers):
            for n, pos in rowNums:
                self.addAdjecency(n, i, *pos)

    def addAdjecency(self, n, y, x1, x2):
        for row in range(max(y-1,0),min(y+2, len(gears)-1)):
            for starX, adjecent in self.gears[row]:
                if x1 - 1 <= starX and starX <= x2 + 1:
                    adjecent.append(n)
                    return True
        return False


elements, gears = EngineSchematicParser(r"2023\D3\D3.txt").getElements()
print(EnginePartGetter(elements, gears).getGearRatio())