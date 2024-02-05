import sys

#defining the world map
worldMap = [['#', '#', '#', '#', '-', '-', '#', '-'],
            ['#', '.', '.', '#', '-', '#', '.', '#'],
            ['#', '.', '.', '#', '-', '#', '.', '#'],
            ['#', '.', '.', '#', '#', '#', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#']]

#player class
class Player:
    
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = [1, 1]
        
    def positionChange(self, position):
        self.position = position
        
    
#function to print the world map
def printMap(worldMap):
    
    print("printing map...")
    print()
    
    for i in range(len(worldMap)):
        for j in range(len(worldMap[i])):
            if worldMap[i][j] == '-':
                print(" ", end = "")
            elif [i, j] == Jimmy.position:
                print("1", end = "")
            else:
                print(worldMap[i][j], end = "")
        print()


#menu for various player actions
def menu():
    
    print()
    print("1. Move")
    print("2. Attack")
    print("3. Use Item")
    print("4. Show Map")
    print("5. Quit")
    print()
    
    choice =  input("Choose your option number: ")
    
    valid = ['1', '2', '3', '4', '5']
    
    #controls input that isn't correct
    while choice not in valid or not choice.isnumeric():
        print("Oops, that's not one of the options...")
        print("Try again!!")
        
        choice = input("Choose your option number: ")
    
    return choice

#updates the player's position based on their chosen move
def movement():

    while True:
        
        validDirections = ["left", "right", "up", "down", "back"]
        
        playerMove = input("Where do you want to go?: ")
        
        #check if the players movement choice is a valid string
        while not playerMove.lower() in validDirections:
            print("Incorrect input...Try again!")
            print()
            playerMove = input("Where do you want to go?: ")
        
        
        #checks if the player has hit a wall or not
        if playerMove.lower() == "right":
            
            y, x = Jimmy.position
            
            if worldMap[y][x + 1] != '#':
                Jimmy.position = [y, x + 1]
                break
            else:
                print("You've hit a wall...")
                print("Try another direction...")
                print()
                continue
            
        elif playerMove.lower() == "left":
            
            y, x = Jimmy.position
            
            if worldMap[y][x - 1] != '#':
                Jimmy.position = [y, x - 1]
                break
            else:
                print("You've hit a wall...")
                print("Try another direction")
                print()

                continue
            
        elif playerMove.lower() == "down":
            
            y, x = Jimmy.position
            
            if worldMap[y + 1][x] != '#':
                Jimmy.position = [y + 1, x]
                break
            else:
                print("You've hit a wall...")
                print("Try another direction")
                print()

                continue
        
        elif playerMove.lower() == "up":
            
            y, x = Jimmy.position
            
            if worldMap[y - 1][x] != '#':
                Jimmy.position = [y - 1, x]
                break
            else:
                print("You've hit a wall...")
                print("Try another direction")
                print()

                continue
        
        elif playerMove.lower() == "back":
            print("Going back to the menu...")
            break
        
        
            
#function for calling methods based on player choice
def choiceControl(choice):
    if choice == '1':
        movement()
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        print()
        printMap(worldMap)
        print()
        
    elif choice == '5':
        print()
        print("Thanks for playing!!")
        sys.exit()


#main game loop
def main():
    
    while True:
        
        playerChoice = menu()
        
        choiceControl(playerChoice)
        
Jimmy = Player("Jimmy", 400, [1, 1])

main()