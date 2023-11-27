import climage

class Player():
    def __init__ (self):
        self.health = 100
        self.inventory = []


for i in range(3):
    print()



map = [[0, 1, 0, 1, 0],
       [1, 1, 0, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 1, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]

#Algorithm to print the map
for i in range(len(map)):

    mapStorage = []

    for j in range(len(map[i])):
        mapStorage.append(map[i][j])
    
    for k in range(3):
        for l in range(len(mapStorage)):
            if mapStorage[l] == 1:
                print("*******", end="")
            else:
                print("   -   ", end="")
        print()
    
#function for welcoming message to player
def welcomeMessage():
    print("Welcome to Fantasy RPG...")    
    print("This game is meant to be a text-adventure game...")
    print("Type any of the options below...")
    print()

#printing various commands
def menu():
    print("MENU: ")
    print("  1. Play")
    print("  2. Tutorial Page")
    print("  3. Quit")
    print()

    return input("Enter in your option number: ")

#function for main gamePlay
def mainGame():

    welcomeMessage()

    #Initializing the variable to hold the player's choice from the menu
    playerOption = ""

    while True:


        playerOption = menu()

        


mainGame()

    
