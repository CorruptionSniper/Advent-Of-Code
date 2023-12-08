LB = 0
LB_PREV = 1
SIZE = 2
class MapParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getSeedRanges(self):
        sR = [int(seed) for seed in self.lines[0][7:].split()]
        return [[sR[i],sR[i],sR[i+1]] for i in range(0,len(sR),2)]

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

X1, X2, L, R = 0, 1, 2, 3
class SeedMapper():
    def __init__(self, seeds, seedMaps):
        self.seedRanges = seeds
        self.seedMappings = seedMaps

    def getMappedRanges(self):
        seedRanges = self.seedRanges
        for mapping in self.seedMappings:
            for seedMap in mapping:
                i = 0
                while i < len(seedRanges):
                    offset, seedRanges[i:i+1] = self.mapSeed(seedRanges[i], seedMap)
                    i += offset
            for i in range(len(seedRanges)):
                seedRanges[i][LB_PREV] = seedRanges[i][LB]
        return seedRanges
    
    
    def mapSeed(self, seedRange, seedMap):
        partitions = self.partitionRange(seedRange[LB_PREV], seedRange[LB_PREV] + seedRange[SIZE], seedMap[LB_PREV], seedMap[LB_PREV] + seedMap[SIZE])
        if partitions:
            ranges = []
            for i in range(len(partitions)-1):
                ranges.append(self.mappedPartition([partitions[i], partitions[i]-seedRange[LB]+seedRange[LB_PREV], partitions[i+1]-partitions[i]], seedMap))
            return len(ranges), ranges
        return 1, [seedRange]
    
    #seedRangeInitial - seedMap[LB_PREV] + seedMap[LB]
    def mappedPartition(self, partition, seedMap):
        if self.inRange(partition, seedMap):
            partition[LB] += seedMap[LB] - seedMap[LB_PREV]
        return partition
    
    def inRange(self, partition, seedMap):
        return seedMap[LB_PREV] <= partition[LB_PREV] < seedMap[LB_PREV] + seedMap[SIZE]
    
    def partitionRange(self, *bounds):
        include = [True]*4
        if bounds[X2] <= bounds[L] or bounds[X1] >= bounds[R]:
            return None
        include[L] = bounds[X1] < bounds[L]
        include[R] = bounds[X2] > bounds[R]
        return sorted([bounds[i] for i in range(4) if include[i]])

p = MapParser(r"2023\D5\D5.txt")
seedRanges = p.getSeedRanges()
mappings = p.getMappings()
r = SeedMapper(seedRanges, mappings).getMappedRanges()
print(min(r)[0])