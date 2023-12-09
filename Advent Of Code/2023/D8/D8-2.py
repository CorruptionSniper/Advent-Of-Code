from math import sqrt, ceil

L, R = 0, 1
LAST_LS, VALS = 0, 1
class MapParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getDirections(self):
        return [L if x == 'L' else R for x in self.lines[0]]
    
    def getListMap(self):
        desertListMap = [[],[]]
        d = self.getDictMap()
        desertListMap[LAST_LS] = list(d.keys())
        desertListMap[VALS] = [[desertListMap[LAST_LS].index(value) for value in d[key]] for key in d.keys()]
        desertListMap[LAST_LS] = [x[-1] for x in desertListMap[LAST_LS]]
        return desertListMap

    def getDictMap(self):
        parsedLines = [line.split(' = ') for line in self.lines[2:]]
        desertMap = {line[0]:line[1].strip('()\n').split(', ') for line in parsedLines}
        return desertMap

class Navigator():
    def __init__(self, desertMap, directions):
        self.directions = directions
        self.map = desertMap

    def getSteps(self, pointer):
        i = 0
        direction = 0
        mod = len(self.directions) - 1
        while self.map[LAST_LS][pointer] != 'Z':
            direction = self.directions[i % mod]
            pointer = self.map[VALS][pointer][direction]
            i += 1
        return i

class Primes(): 
    def __init__(self, maxN):
        self.primes = Primes.primes(maxN)
    
    @staticmethod
    def primes(n):
        primes = [0, 0] + [True]*int(n-1)
        step = 2
        while step < len(primes):
            for i in range(2*step, len(primes), step):
                primes[i] = False
            step += 1
            while step < len(primes) and not primes[step]:
                step += 1
        return [i for i, x in enumerate(primes) if x]

    def primeFactor(self, n):
        primeFactors = [0] * len(self.primes)
        for i, p in enumerate(self.primes):
            if n == 1:
                break
            q, r = divmod(n, p)
            while not r:
                primeFactors[i] += 1
                n = q
                q, r = divmod(n, p)
        return primeFactors

    def lCM(self, nums):
        return self.primeProduct(self.pFactorsLCM(nums))

    def pFactorsLCM(self, nums):
        numsPFactors = [self.primeFactor(n) for n in nums]
        return [max([p[i] for p in numsPFactors]) for i in range(len(self.primes))]

    def primeProduct(self, pFactors):
        rProd = 1
        for i in range(len(self.primes)):
            if pFactors[i]:
                rProd *= self.primes[i]**pFactors[i]
        return rProd

parser = MapParser(r"2023\D8\D8.txt")
directions = parser.getDirections()
desertMap = parser.getListMap()
stepsToLoop = [Navigator(desertMap, directions).getSteps(i) for i in range(len(desertMap[LAST_LS])) if desertMap[LAST_LS][i] == 'A']
print(Primes(max(stepsToLoop)).lCM(stepsToLoop))