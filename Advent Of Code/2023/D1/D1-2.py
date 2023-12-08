DIGITS = ['0','1','2','3','4','5','6','7','8','9']
WORDDIGITS = ['one','two','three','four','five','six','seven','eight','nine']
class DocumentParser():
    def __init__(self, filename=None):
        if filename is not None:
            f = open(filename, 'r')
            self.lines =  f.readlines()
            f.close()

    def getCalibrationSum(self):
        runningSum = 0
        for line in self.lines:
            runningSum += self.get2DigitN(line)
        return runningSum

    def get2DigitN(self, line):
        i = self.findDigit(line, 1)
        j = self.findDigit(line, -1)
        return 10*i + j
    
    def findDigit(self, line, direction):
        i = 0 if direction == 1 else len(line) - 1
        iWords = [0]*9
        while line[i] not in DIGITS:
            for iWord in range(len(WORDDIGITS)):
                if line[i] == WORDDIGITS[iWord][direction*iWords[iWord] - (direction == -1)]:
                    iWords[iWord] += 1
                    if iWords[iWord] == len(WORDDIGITS[iWord]):
                        return iWord + 1
                else:
                    start = max(i-iWords[iWord],0) if direction == 1 else i
                    end = i + 1 if direction == 1 else min(i + iWords[iWord],len(line)-1)
                    iWords[iWord] = self.maxSize(line[start:end], iWord, iWords[iWord], direction)
            i += direction
        return DIGITS.index(line[i])
    
    def maxSize(self, line, iWord, size, direction):
        size += 1
        i = 0
        if direction == 1:
            while size and line[i:] != WORDDIGITS[iWord][:-i or None]:
                i += 1
                size -= 1
        else:
            while size and line[:-i or None] != WORDDIGITS[iWord][i:]:
                i += 1
                size -= 1
        return size

print(DocumentParser("Advent Of Code\\2023\\D1\\D1.txt").getCalibrationSum())