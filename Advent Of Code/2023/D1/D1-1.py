DIGITS = ['0','1','2','3','4','5','6','7','8','9']
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
        for i in line[::direction]:
            if 48 <= ord(i) < 58:
                return DIGITS.index(i)

print(DocumentParser("Advent Of Code\\2023\\D1\\D1.txt").getCalibrationSum())