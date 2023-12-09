JOKER = 'J'
SYMBOLS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', JOKER][::-1]
SYMBOL_RANKS = {symbol:i for i,symbol in enumerate(SYMBOLS, 1)}
BASE = len(SYMBOLS) + 1

HAND, BID = 0, 1
class CamelCardsParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()

    def getHands(self):
        hands = []
        for line in self.lines:
            sLine = line.split()
            hands.append((sLine[HAND],int(sLine[BID])))
        return hands

class CamelCards():
    def __init__(self, hands):
        self.hands = hands

    def getWinnings(self):
        self.hands = sorted(self.hands,key=lambda hand: CamelCards.cardRankValue(hand[HAND]))
        return [x[BID]*i for i, x in enumerate(self.hands, 1)]

    @staticmethod
    def cardRankValue(card):
        return CamelCards.cardTypeValue(card)*(BASE**6) + CamelCards.cardScoreValue(card)
    
    """
    Type      Value  True 
    5ofKind   6      Max 5
    4ofKind   5      Max 4
    FullHouse 4      Max 3 sMax 2
    3ofKind   3      Max 3
    2pair     2      Max 2 sMax 2
    1pair     1      Max 2
    1ofkind   0      Max 1
    """
    @staticmethod
    def cardTypeValue(card):
        symbol_categories = {symbol:card.count(symbol) for symbol in SYMBOLS[1:]}
        symbolMaxs = [0, 0]
        for nSymbol in symbol_categories.values():
            if nSymbol > symbolMaxs[0]:
                symbolMaxs[1] = symbolMaxs[0]
                symbolMaxs[0] = nSymbol
            elif nSymbol > symbolMaxs[1]:
                symbolMaxs[1] = nSymbol
        jokers = card.count(JOKER)
        if symbolMaxs[0] + jokers > 3: #0 <= jokers <= 5, No 5K, 4K
            return symbolMaxs[0] + jokers + 1
        elif symbolMaxs[0] + jokers == 3: #0 <= jokers <= 3, No 3K, FH
            return 3 + (symbolMaxs[1] == 2)
        elif symbolMaxs[0] == 2: #0 <= jokers <= 2, Either 2P, 1P, or 1K
            return 1 + (symbolMaxs[1] + jokers == 2)
        #Either 2K or 1K
        return symbolMaxs[0] + jokers - 1
    
    """
    Converts card into a number base <#Symbols + 1>.
    """
    @staticmethod
    def cardScoreValue(card):
        rSum = 0
        p = 1
        for letter in card[::-1]:
            rSum += SYMBOL_RANKS[letter]*p
            p *= BASE
        return rSum 

#print(CamelCards.cardTypeValue('224JJ'))   
hands = CamelCardsParser(r"2023\D7\D7.txt").getHands()
print(sum(CamelCards(hands).getWinnings()))