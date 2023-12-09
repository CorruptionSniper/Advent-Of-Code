import numpy

class SensorDataParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()
    
    def getSequences(self):
        sequences = []
        for line in self.lines:
            sequences.append([int(x) for x in line.split()])
        return sequences
    
class SequenceSolver():
    @staticmethod
    def getNextElement(sequence):
        if len(sequence):
            return sequence[-1] + SequenceSolver.getNextElement([sequence[i+1]-sequence[i] for i in range(len(sequence)-1)])
        return 0
    
    @staticmethod
    def getPrevElement(sequence):
        if len(sequence):
            return sequence[0] - SequenceSolver.getPrevElement([sequence[i+1]-sequence[i] for i in range(len(sequence)-1)])
        return 0

sequences = SensorDataParser(r"2023\D9\D9.txt").getSequences()
print(sum([SequenceSolver.getPrevElement(sequence) for sequence in sequences]))