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
        nList = self.getAllDigits(line)
        return 10*nList[0] + nList[-1]
    
    def getAllDigits(self, line):
        nList = []
        for i in range(len(line)):
            if line[i] in DIGITS:
                nList.append(DIGITS.index(line[i]))
            for j, wDigit in enumerate(WORDDIGITS):
                if wDigit == line[i:i+len(wDigit)]:
                    nList.append(j + 1)
        return nList
    
    def findAll(self, sub, string, i):
        try:
            string[i:].index(sub[0])
        except ValueError:
            return []

print(DocumentParser(r"2023\D1\D1.txt").getCalibrationSum())