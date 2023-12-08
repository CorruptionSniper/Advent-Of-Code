DIGITS = ['0','1','2','3','4','5','6','7','8','9']
BASE_SYMBOL = '.'
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
        symbols = [[] for x in range(len(self.lines))]
        for row, line in enumerate(self.lines):
            n, i, j = self.getNumber(line, 0)
            while j != len(line):
                numbers[row].append((n, (i, j)))
                n, i, j = self.getNumber(line, j + 1)
            symbols[row] = self.getSymbols(line)
        return numbers, symbols
    
    def getNumber(self, line, i):
        while i != len(line) and line[i] not in DIGITS:
            i += 1
        if i != len(line):
            j = i + 1
            while j != len(line) and line[j] in DIGITS:
                j += 1
            return int(line[i:j]), i, j - 1
        return None, None, len(line)
    
    def getSymbols(self, line):
        symbols = []
        i = 0
        while i != len(line[:-2]):
            nI = ord(line[i])
            if (nI < 48 or nI > 57) and nI != 46:
                symbols.append(i)
            i += 1
        return symbols

class EnginePartGetter():
    def __init__(self, numbers, symbols):
        self.numbers = numbers
        self.symbols = symbols

    def getPartNumbers(self):
        partNumbers = []
        for i, rowNums in enumerate(self.numbers):
            for n, pos in rowNums:
                if self.isAdjecentToSymbols(i, *pos):
                    partNumbers.append(n)
        return partNumbers

    def isAdjecentToSymbols(self, y, x1, x2):
        for row in range(max(y-1,0),min(y+2, len(symbols)-1)):
            for starX in self.symbols[row]:
                if x1 - 1 <= starX and starX <= x2 + 1:
                    return True
        return False


elements, symbols = EngineSchematicParser("Advent Of Code\\2023\\D3\\D3.txt").getElements()
print(sum(EnginePartGetter(elements, symbols).getPartNumbers()))