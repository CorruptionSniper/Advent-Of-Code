X, Y = 0, 1
class PatternParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getPatterns(self):
        patterns = [[]]
        for line in [line.strip('\n') for line in self.lines]:
            if line:
                patterns[-1].append(line)
            else:
                patterns.append([])
        return patterns

class PatternWrapper():
    def __init__(self, pattern):
        self.pattern = pattern

    def isLineOfSymmetry(self, p, direction):
        self.conflicts = 0
        return self.__xSymmetry(p) if direction == X else self.__ySymmetry(p)

    def __xSymmetry(self, x):
        size = min(x,len(self.pattern[0])-x)
        for row in self.pattern:
            for i1, i2 in zip(range(x,x+size+1),range(x-1,x-size-1,-1)):
                if row[i1] != row[i2]:
                    self.conflicts += 1
                if self.conflicts == 2:
                    return False
        return self.conflicts == 1

    def __ySymmetry(self, y):
        size = min(y,len(self.pattern)-y)
        for cI in range(len(self.pattern[0])):
            for i1, i2 in zip(range(y,y+size+1),range(y-1,y-size-1,-1)):
                if self.pattern[i1][cI] != self.pattern[i2][cI]:
                    self.conflicts += 1
                if self.conflicts == 2:
                    return False
        return self.conflicts == 1

class PatternAnalyser():
    def __init__(self, patterns):
        self.patterns = patterns

    def reflectionLinePatternsSum(self):
        rLPsum = [0,0]
        for direction in [X, Y]:
            for pattern in self.patterns:
                rLPsum[direction] += sum(self.__reflections(pattern,direction))
        return 100*rLPsum[Y] + rLPsum[X]
    
    def __reflections(self, pattern, direction):
        wrapper = PatternWrapper(pattern)
        lines = len(pattern[0]) if direction == X else len(pattern)
        return [i for i in range(1,lines) if wrapper.isLineOfSymmetry(i,direction)]


parser = PatternParser(r"2023\D13\D13.txt")
patterns = parser.getPatterns()
print(PatternAnalyser(patterns).reflectionLinePatternsSum())