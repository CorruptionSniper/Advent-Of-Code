ID = 0
ROUNDS = 1
COLOURS = ['red','green','blue']
class GameRecordParser():
    def __init__(self, filename):
        f = open(filename)
        self.lines = f.readlines()
        f.close()
    
    def getGames(self):
        games = []
        for line in self.lines:
            game = line.split(':')
            rounds = []
            for gameRound in game[ROUNDS].split(';'):
                rounds.append(self.getRoundColours(gameRound))
            games.append([int(game[ID].split(' ')[1]),rounds])
        return games
    
    def getRoundColours(self, gameRound):
        roundColours = [0,0,0]
        for Ncolour in gameRound.strip().split(','):
            Ncolour = Ncolour.strip().split(' ')
            roundColours[COLOURS.index(Ncolour[1])] = int(Ncolour[0])
        return roundColours
    
class PossibleGames():
    def __init__(self, games, possibleGame):
        self.games = games
        self.possibleGame = possibleGame

    def getPossibleGames(self):
        maxColoursFromGames = ((game[ID],self.getMaxFromGame(game[ROUNDS])) for game in self.games)
        possibleGames = []
        for gameId, maxColours in maxColoursFromGames:
            if self.isPossible(maxColours):
                possibleGames.append(gameId)
        return possibleGames

    def getMaxFromGame(self, rounds):
        maxColours = [0,0,0]
        for gameRound in rounds:
            for colour in range(3):
                maxColours[colour] = max(maxColours[colour],gameRound[colour])
        return maxColours
    
    def isPossible(self, maxColours):
        for i in range(3):
            if self.possibleGame[i] < maxColours[i]:
                return False
        return True

games = GameRecordParser(r"2023\D2\D2.txt").getGames()
print(sum(PossibleGames(games,[12,13,14]).getPossibleGames()))
