from terminal_playing_cards import Deck
from terminal_playing_cards import View
import time

def war(ties, warBoard, warCount, winningCards):
    

    #Checking if all the players can enter war, and determining the
    
    if len(ties[0].hand) < (warCount + 1):
        print(ties[0].name + "does not have enough cards to go to war...")
        print("This means that " + ties[1].name + " is automatically the winner!!")
        print("Congratulations" + ties[1].name + "!")
        #--------------Testing outputs-----------------------------------------------------
        for i in range(len(warBoard.players_list)):
            print(len(warBoard.players_list[i].hand))
            #----------------------------------------------------------------------------------
        quit()

        

    elif len(ties[1].hand) < (warCount + 1):
        time.sleep(1.5)
        print(ties[1].name + " does not have enough cards to go to war...")
        time.sleep(1.5)
        print("This means that " + ties[0].name + " is automatically the winner!!")
        time.sleep(1.5)
        print("Congratulations " + ties[0].name + "!")

        print()

        #--------------Testing outputs-----------------------------------------------------
        for i in range(len(warBoard.players_list)):
            print(warBoard.players_list[i].name + str(len(warBoard.players_list[i].hand)))
            #----------------------------------------------------------------------------------
        quit()


    time.sleep(1.5)

    print("There has been a tie for the highest card...")

    time.sleep(1.5)
    
    print("We must now go to war")

    time.sleep(1.5)

    print("First we'll put the cards face down...")

    time.sleep(1.5)


    for i in range(len(ties)):
        for j in range(warCount):

            print("It is " + warBoard.players_list[i].name + "'s turn...")

        

            playerInput = input("Press 'enter' to draw a card:")

            


            print(ties[i].name + " draws a card and puts it in the pile")

            currentView = View([])

            cardToPlace = ties[i].hand.pop()

            cardToPlace.hidden = True

            currentView += [cardToPlace]

            print(currentView)

            winningCards.append(cardToPlace)
    
    time.sleep(1.5)
    print("Now we place more cards face-up to see who wins all these cards...")

    faceUpViewAll = View([])

    warPlayersAndTheirCards = []

    for i in range(len(ties)): 

        warPlayerCardToAdd = []

        warCardDrawn = ties[i].hand.pop()


        currentView = View([])

        currentView += [warCardDrawn]
        
        faceUpViewAll += [warCardDrawn]

        print(currentView)

        if warCardDrawn.value > 10:
            currentPlayer = ties[i].name
            valueToFace(warCardDrawn, currentPlayer)
        else:
            print(ties[i].name + " has drawn a " + str(warCardDrawn.value) + " of " + warCardDrawn.suit)
            print()
        
        warPlayerCardToAdd.append(ties[i])
        warPlayerCardToAdd.append(warCardDrawn)


        warPlayersAndTheirCards.append(warPlayerCardToAdd)
        

    print("Here's all the player's cards...")

    print(faceUpViewAll)

    maxValue = warPlayersAndTheirCards[0][1].value
    maxPlayer = warPlayersAndTheirCards[0][0]

    #finding the biggest card this round for war 
    for i in range(len(warPlayersAndTheirCards)):
        if warPlayersAndTheirCards[i][1].value > maxValue:
            maxValue = warPlayersAndTheirCards[i][1].value
            maxPlayer = warPlayersAndTheirCards[i][0]

    ties = []

    #checking for ties for war rules
    for i in range(len(warPlayersAndTheirCards)):
        if warPlayersAndTheirCards[i][1].value == maxValue:
            ties.append(warPlayersAndTheirCards[i][0])
    
    warWinningCards = []

    if len(ties) < 2:
        print()
        time.sleep(1.5)
        print(maxPlayer.name + " wins with the highest card!!")
        
        
        #Distributing all the cards to the winning players hand
        for i in range(len(warPlayersAndTheirCards)):
            warWinningCards.append(warPlayersAndTheirCards[i][1])
        
        winningCards = winningCards + warWinningCards
        print(maxPlayer.name + " you have won " + str(len(winningCards)) + " cards... Congratulations!!")
        maxPlayer.hand = maxPlayer.hand + winningCards

        #Changing all cards in the players decks to face up for re-playability
        for i in range(len(warBoard.players_list)):
            for j in range(len(warBoard.players_list[i].hand)):
                warBoard.players_list[i].hand[j].hidden = False


    else:
        
        for i in range(len(warPlayersAndTheirCards)):
            warWinningCards.append(warPlayersAndTheirCards[i][1])

        winningCards = winningCards + warWinningCards
        warCount += 1

        #Changing all cards in the players decks to face up for re-playability
        for i in range(len(warBoard.players_list)):
            for j in range(len(warBoard.players_list[i].hand)):
                warBoard.players_list[i].hand[j].hidden = False


        war(ties, warBoard, warCount, winningCards)
def valueToFace(currentPlayerTopCard, currentPlayer):

    if currentPlayerTopCard.value == 11:
        time.sleep(1.5)
        print(currentPlayer + " has drawn a Jack of " + currentPlayerTopCard.suit)
        time.sleep(1.5)
        print()
       
    elif currentPlayerTopCard.value == 12:
        time.sleep(1.5)
        print(currentPlayer + " has drawn a Queen of " + currentPlayerTopCard.suit)
        time.sleep(1.5)
        print()
      
    elif currentPlayerTopCard.value == 13:
        time.sleep(1.5)
        print(currentPlayer + " has drawn a King of " + currentPlayerTopCard.suit)
        time.sleep(1.5)
        print()
      
    elif currentPlayerTopCard.value == 14:
        time.sleep(1.5)
        print(currentPlayer + " has drawn an Ace of " + currentPlayerTopCard.suit)
        time.sleep(1.5)
        print()
        
def cardAllocation(warBoard, player_count):

    warBoard.main_deck.shuffle()

    for i in range(52):
        if warBoard.main_deck[i].value == 1:
            warBoard.main_deck[i].value = 14
    
    for i in range(int(player_count)):
        for j in range(52 // player_count):
            warBoard.players_list[i].hand.append(warBoard.main_deck.pop())

    #------------------------------------------
def addPlayers(warBoard, player_count):
    for i in range(int(player_count)):
        player_name = input("Please enter in the player's name: ")

        warBoard.players_list.append(Player(player_name))

    print()

def mainGame(warBoard, player_count):
    
    gameEnd = False


    winner = ""
    loser = ""

    while True:


    #re-indent this variable when using the while-loop 

    #re-indent this for loop when using the while-loop 
        if len(warBoard.players_list[0].hand) == 52 or len(warBoard.players_list[0].hand) == 0:
            if len(warBoard.players_list[0].hand) == 52:
                winner = warBoard.players_list[0].name
                loser = warBoard.players_list[1].name
                gameEnd = True
            elif len(warBoard.players_list[0].hand) == 0:
                loser = warBoard.players_list[0].name
                winner = warBoard.players_list[1].name
                gameEnd = True
    
    #re-indent this if-statement when using the while-loop    
        if gameEnd == True:
            #This break is for the while loop
            break

            
            

        allPlayersView = View([])

        playersAndTheirCards = []

    #re-indent
        for i in range(player_count):

            playerAndCardToAdd = []
        
            currentPlayerView = View([])

            currentPlayerTopCard = warBoard.players_list[i].hand.pop()

            allPlayersView += [currentPlayerTopCard]
            currentPlayerView += [currentPlayerTopCard]


        #--------------------IN PROGRESS -------------------------------------

            print("It is " + warBoard.players_list[i].name + "'s turn...")

            time.sleep(1)

            playerInput = input("Press 'enter' to draw a card:")

            print(warBoard.players_list[i].name + " has drawn their top card ...")
            print(currentPlayerView)

            if currentPlayerTopCard.value > 10:
                currentPlayer = warBoard.players_list[i].name
                valueToFace(currentPlayerTopCard, currentPlayer)
            else:
                time.sleep(1.5)
                print(warBoard.players_list[i].name + " has drawn a " + str(currentPlayerTopCard.value) + " of " + currentPlayerTopCard.suit)
                time.sleep(1.5)
                print()

            playerAndCardToAdd.append(warBoard.players_list[i])
            playerAndCardToAdd.append(currentPlayerTopCard)

            playersAndTheirCards.append(playerAndCardToAdd)

        #---------------------------------------------------------------------

    
    #spacing
        for i in range(2):
            print()

        print("Here's all the player's cards...")
        print(allPlayersView)

        maxValue = playersAndTheirCards[0][1].value
        maxPlayer = playersAndTheirCards[0][0]

    #finding the biggest card this round
        for i in range(len(playersAndTheirCards)):
            if playersAndTheirCards[i][1].value > maxValue:
                maxValue = playersAndTheirCards[i][1].value
                maxPlayer = playersAndTheirCards[i][0]

        ties = []

    #checking for ties for war rules
        for i in range(len(playersAndTheirCards)):
            if playersAndTheirCards[i][1].value == maxValue:
                ties.append(playersAndTheirCards[i][0])
    
        winningCards = []

        if len(ties) < 2:
            print()
            time.sleep(1.5)
            print(maxPlayer.name + " wins with the highest card!!")
            time.sleep(1.5)
            print(maxPlayer.name + " you have won " + str(len(allPlayersView)) + " cards... Congratulations!!")
            print()

            
        
        #Distributing all the cards to the winning players hand
            for i in range(len(playersAndTheirCards)):
                winningCards.append(playersAndTheirCards[i][1])
        
            maxPlayer.hand = maxPlayer.hand + winningCards

            
        else:
        
            for i in range(len(playersAndTheirCards)):
                winningCards.append(playersAndTheirCards[i][1])

            warCount = 1
            war(ties, warBoard, warCount, winningCards)
    
    #--------------Testing outputs-----------------------------------------------------
    for i in range(len(warBoard.players_list)):
        print(warBoard.players_list[i].name + str(len(warBoard.players_list[i].hand)))
            #----------------------------------------------------------------------------------
    print("Looks like someone has all the cards...")
    print("The winner is " + winner + "!!!")
    print("Congratulations " + winner + "!!")

def play():

    warBoard = Board()

    player_count = 2

    print("War only has two players, sorry for any other people...")

    addPlayers(warBoard, player_count)
    
    cardAllocation(warBoard, player_count)

    mainGame(warBoard, player_count)

class Board:
    def __init__(self):
        self.board_cards = []
        self.main_deck = Deck()
        self.players_list = []
class Player: 
    def __init__(self, name):
        self.name = name
        self.hand = []

#-----------------------------
print("Welcome to War!!")
#----

play()