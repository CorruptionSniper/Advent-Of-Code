LB = 0
LB_PREV = 1
SIZE = 2
class MapParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getSeeds(self):
        return [int(seed) for seed in self.lines[0][7:].split()]

    def getMappings(self):
        mapping = []
        isMapping = False
        for line in self.lines[1:]:
            if isMapping and 48 <= ord(line[0]) < 58:
                mapping[-1].append([int(x) for x in line.split()])
            elif line[0] == '\n':
                isMapping = False
            else:
                mapping.append([])
                isMapping = True
        return mapping

class SeedMapper():
    def __init__(self, seeds, seedMaps):
        self.seeds = seeds
        self.seedMappings = seedMaps

    def getMappedSeeds(self):
        for mapping in self.seedMappings:
            self.seeds = self.mapSeeds(self.seeds, mapping)
        return self.seeds

    def mapSeeds(self, seeds, mapping):
        for seedMap in mapping:
            seeds = [self.mapSeed(seedInitial, seed, seedMap) for seed, seedInitial in zip(seeds, self.seeds)]
        return seeds
    
    def mapSeed(self, seedInitial, seed, seedMap):
        if seedMap[LB_PREV] <= seedInitial < seedMap[LB_PREV] + seedMap[SIZE]:
            return seed - seedMap[LB_PREV] + seedMap[LB]
        return seed

p = MapParser(r"2023\D5\D5.txt")
seeds = p.getSeeds()
mappings = p.getMappings()
print(min(SeedMapper(seeds, mappings).getMappedSeeds()))