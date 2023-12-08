ID = 0
CARD = 1
WIN = 0
INV = 1
class ScratchCardParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()
    
    def getCards(self):
        cards = []
        for line in self.lines:
            idCard = line.split(':')
            card = [[int(num) for num in nums.split()] for nums in idCard[CARD].split('|')]
            cards.append((int(idCard[ID][5:].strip()),card))
        return cards

class ScracthCardGame():
    def __init__(self, cards):
        self.cards = cards

    def getWinningNumbers(self):
        return [(cardID, [win for win in card[WIN] if win in card[INV]]) for cardID, card in self.cards]

    def getScore(self):
        return sum([len(wins) and 1<<(len(wins)-1) for cardID, wins in self.getWinningNumbers()])

cards = ScratchCardParser("Advent Of Code\\2023\\D4\\D4.txt").getCards()
print(ScracthCardGame(cards).getScore())