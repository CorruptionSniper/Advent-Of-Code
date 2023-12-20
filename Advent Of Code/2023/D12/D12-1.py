ROW = 0
PARTITIONS = 1

PLACEMENT, EMPTY, DAMAGED = '?', '.', '#'
class RecordParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getRows(self):
        rows = []
        for line in self.lines:
            sLine = line.split()
            rows.append([sLine[0], [int(x) for x in sLine[1].strip().split(',')]])
        return rows

def allSatified(array):
    for element in array:
        if element:
            return False
    return True

def nextConsecutive(array, symbol, i=0, limit=-1):
    try:
        return consecutive(array, symbol, array.index(symbol,i), limit)
    except ValueError:
        return len(array), 0

def consecutive(array, symbol, i=0, limit=-1):
    limit %= len(array)
    j = i
    while j <= limit and array[j] == symbol:
        j += 1
    return j, j - i

class RecordAnalyser():
    def getNPermutations(self, row, i=0):
        if not self.isValid(row, i):
            return 0
        if (i := self.getNextPlacement(row, i)) == -1:
            return self.isValid(row, i)
        return sum([self.getNPermutations(row,i+1) for row in self.permutations(row, i)])

    def permutations(self, row, i):
        r = row[ROW]
        return [[str(r[:i] + symbol + r[i+1:]),row[PARTITIONS]] for symbol in [EMPTY,DAMAGED]]

    def isValid(self, row, i=-1):
        partitions = self.getPartitions(row, i)
        if i == -1:
            return partitions == row[PARTITIONS]
        for partition, correctPartition in zip(partitions,row[PARTITIONS]):
            if partition > correctPartition:
                return False
        return True

    def getPartitions(self, row, limit=-1):
        r = row[ROW]
        if limit == -1:
            limit += len(r)
        else:
            limit = min(limit, len(r)-1)
        partitions = []
        j = 0
        while j < limit:
            j, partition = nextConsecutive(r, DAMAGED, j, limit)
            if partition:
                partitions.append(partition)
        return partitions
    
    def getNextPlacement(self, row, i=0):
        try:
            return row[ROW].index(PLACEMENT, i)
        except ValueError:
            return -1

parser = RecordParser(r"2023\D12\D12.txt")
rows = parser.getRows()
print(sum([RecordAnalyser().getNPermutations(row) for row in rows]))