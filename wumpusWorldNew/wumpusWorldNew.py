from collections import OrderedDict
import random
import math

#Acronym Meanings for convenience
#St - Stench
#W - Wumpus
#B - Breeze
#S - Start
#P - Pit
#G - Glitter/Gold

gold = "unfound"

#Sensors for the agent
#Stench, Breeze, Glitter, Scream

#Intead of having "Bump,", we'll have the agent know when they're in a wall or a corner based on what they "percieve"

#Storing where the agent has already been
visitedSquares = set()

#Storing possible spots for pits/wumpus based on the agents "knowledge"
possiblePits = set()
possibleWumpus = set()
safeSpots = set()

#Defining maximum lengths for the grid
minimum = 0
maximum = 3

#split() functions will be used to parse multiple strings which mean multiple things were "sensed" by the agent
worldMap = [["Stench",           "0",                "Breeze", "Pit"],
            ["Wumpus", "Breeze Stench Glitter",    "Pit",    "Breeze"],
            ["Stench",           "0",                "Breeze",     "0"],
            ["Start Player",         "Breeze",            "Pit",    "Breeze"]]

#Declaring possible moves for the agent at any given time
possibleMoves = OrderedDict()

possibleMoves["L"] = [0, -1]
possibleMoves["R"] = [0, 1]
possibleMoves["U"] = [1, 0]
possibleMoves["D"] = [-1, 0]

#Defining corners/walls for the agent to "bump" into

#Also good for having the agent "reason" about obstacles depending on whether 
#they're in the middle of the board, in a corner, or on the edge
corners = {
    "topLeft": [0, 0],
    "topRight": [0, 3], 
    "bottomLeft": [3, 0],
    "bottomRight": [3, 3]
}

walls = {
    "leftWalls": [[1, 0], [2, 0]], 
    "bottomWalls": [[3, 1], [3, 2]],
    "rightWalls": [[1, 3], [2, 3]],
    "topWalls": [[0, 1], [0, 2]]
}

#Initializing the agent at the starting location (bottom-left corner)
agentStart = [3, 0]

unSafeSpots = []

for i in range(len(worldMap)):
    for j in range(len(worldMap)):
        if worldMap[i][j] == "Pit" or worldMap[i][j] == "Wumpus":
            unSafeSpots.append([i, j])

#Makes the chance for the agent to choose a new location greater, simulating real "curiosity"
def newMoveChance():

    moveChance = random.randint(1, 10)

    if moveChance <= 7:
        return True

    return False

#Allows the agent to choose a move
def moveChoice(possibleVisited, possibleUnVisited):
    if not possibleVisited:
        return random.choice(possibleUnVisited)
    elif not possibleUnVisited:
        return random.choice(possibleVisited)
    else:
        if newMoveChance():
            return random.choice(possibleUnVisited)
        else:
            return random.choice(possibleVisited)
#This function prints the world map for the user to see the wumpus, pits and the agent's current location
def printWorld(worldMap, currentLocation):

    for k in range(len(worldMap)):

        stringsInRow = []
        for l in range(len(worldMap[k])):
            stringsInRow.append(worldMap[k][l])

        for j in range(6):
            print()

            for i in range(len(worldMap[k])):
                if j < 1 or j > 4:
                    print("- - - - -", end="")
                else:
                    sensesPrint = stringsInRow[i].split()

                    match len(sensesPrint):
                        case 1:
                            if j == 1:
                                if sensesPrint[0] != '0':
                                    print('|{: >7}|'.format(sensesPrint[0]), end="") 
                                else:
                                    print("|       |", end="")
                            else:
                                print("|       |", end="")
                        case 2:
                            if j == 1:
                                if sensesPrint[0] != '0':
                                    print('|{: >7}|'.format(sensesPrint[0]), end="")
                                else:
                                    print("|       |", end="")
                            elif j == 2:
                                print('|{: >7}|'.format(sensesPrint[1]), end="") 
                            else:
                                print("|       |", end="")
                        case 3:
                            if j == 1:
                               print('|{: >7}|'.format(sensesPrint[0]), end="")
                            elif j == 2:
                                print('|{: >7}|'.format(sensesPrint[1]), end="") 
                            elif j == 3:
                                print('|{: >7}|'.format(sensesPrint[2]), end="") 
                            else:
                                print("|       |", end="")
                        case 4:
                            if j == 1:
                               print('|{: >7}|'.format(sensesPrint[0]), end="")
                            elif j == 2:
                                print('|{: >7}|'.format(sensesPrint[1]), end="") 
                            elif j == 3:
                                print('|{: >7}|'.format(sensesPrint[2]), end="") 
                            elif j == 4:
                                print('|{: >7}|'.format(sensesPrint[3]), end="") 
    print()  
#Intro message for the user running the program 
def welcomeMessage():
    print("Welcome to Wumpus World...")
    print("Let's see what the agent can do...")
#This function passes in everything the agent senses on any given block
def senses(currentLocation):
    
    currentLocationSenses = worldMap[currentLocation[0]][currentLocation[1]].split()

    global gold

    for i in range(len(currentLocationSenses)):
        if currentLocationSenses[i].lower() == "stench":
            calculateWumpus(currentLocation)
        elif currentLocationSenses[i].lower() == "breeze":
            calculatePits(currentLocation)
        elif currentLocationSenses[i].lower() == "glitter":
            gold = "found"
#Has the agent, "think" about where the wumpus could be
def calculateWumpus(currentLocation):
    
    for key, value in possibleMoves.items():
            
        newX, newY = currentLocation[1] + value[1], currentLocation[0] + value[0]

        #We've hit a corner or a wall
        if newX < minimum or newX > maximum or newY < minimum or newY > maximum:
            continue
        
        if [newY, newX] == agentStart or tuple([newY, newX]) in safeSpots:
            continue

        newLocation = [newY, newX]

        possibleWumpus.add(tuple(newLocation))
#Has the agent, "think" about where pits could be on the map
def calculatePits(currentLocation):
    
    for key, value in possibleMoves.items():
            
        newX, newY = currentLocation[1] + value[1], currentLocation[0] + value[0]

        #We've hit a corner or a wall
        if newX < minimum or newX > maximum or newY < minimum or newY > maximum:
            continue

        if [newY, newX] == agentStart or tuple([newY, newX]) in safeSpots:
            continue
            
        newLocation = [newY, newX]

        possiblePits.add(tuple(newLocation))
#Updates the player's location for the printWorld() function
def playerLocationUpdate(currentLocation):
    for i in range(len(worldMap)):
            for j in range(len(worldMap[i])):
                playerRemovalCheck = worldMap[i][j].split()

                if playerRemovalCheck[len(playerRemovalCheck) - 1] == "Player":
                    playerRemovalCheck.pop()

                    worldFix = ""

                    for k in range(len(playerRemovalCheck)):
                        if k == 0:
                            worldFix = worldFix + playerRemovalCheck[k]
                        else:
                            worldFix = worldFix + " " + playerRemovalCheck[k]
                    
                    worldMap[i][j] = worldFix



    for i in range(len(worldMap)):
        for j in range(len(worldMap[i])):
            
            if i == currentLocation[0] and j == currentLocation[1]:
                playerRemovalCheck = worldMap[i][j].split()
                
                worldFix = ""

                for k in range(len(playerRemovalCheck)):
                    if k == 0:
                        worldFix = worldFix + playerRemovalCheck[k]
                    else:
                        worldFix = worldFix + " " + playerRemovalCheck[k]
                
                worldFix = worldFix + " Player"

                worldMap[i][j] = worldFix
#Distance formula for returning to start
def distance(possibleMove, agentStart):

    xValues = possibleMove[1] - agentStart[1]

    yValues = possibleMove[0] - agentStart[0]

    xValuesSquared = xValues * xValues

    yValuesSquared = yValues * yValues

    return math.sqrt(yValuesSquared + xValuesSquared)

#Main function where the agent's game loop will occur
def main():

    welcomeMessage()

    global possiblePits, possibleWumpus, gold, goldFound

    currentLocation = agentStart

    
    

    while gold != "found":   


        printWorld(worldMap, currentLocation)

        playerContinue = ""  

        while playerContinue.lower() != "c":
            playerContinue = input("Type 'c' to see the next choice for the agent: ")


        visitedSquares.add(tuple(currentLocation))


        possibleVisited = []
        possibleUnVisited = []

        for key, value in possibleMoves.items():
            
            newX, newY = currentLocation[1] + value[1], currentLocation[0] + value[0]

            #We've hit a corner or a wall
            if newX < minimum or newX > maximum or newY < minimum or newY > maximum:
                continue
            
            #our new location is in a death spot
            if tuple([newY, newX]) in possiblePits or tuple([newY, newX]) in possibleWumpus:
                continue
            
            newLocation = [newY, newX]

            if tuple(newLocation) in visitedSquares:
                possibleVisited.append(newLocation)
            else:
                possibleUnVisited.append(newLocation)

        currentLocation = moveChoice(possibleVisited, possibleUnVisited)

        #This if-statement will check for any senses for locations that are new
        if tuple(currentLocation) not in visitedSquares:
            senses(currentLocation)
        
        if gold == "found":
            print("THE AGENT HAS FOUND THE GOLD!")
            print("NOW THE AGENT MUST SAFELY MAKE THEIR WAY BACK TO THE START!!")
            
            break

        #Changing the players current location on the worldMap
        #Turn these into functions
        playerLocationUpdate(currentLocation)
        
        #This determines areas that are for sure safe, since there can't be a Wumpus and a Pit in the same spot
        safeArea = possiblePits.intersection(possibleWumpus)

        possibleWumpus -= safeArea
        possiblePits -= safeArea
        
        if safeArea:
            safeList = list(safeArea)
            
            for item in safeList:
                dataCheck = []
                dataCheck.append(item[0])
                dataCheck.append(item[1])
            
            safeSpots.add(tuple(dataCheck))
            
       
        
                   
    playerLocationUpdate(currentLocation)
    
    while currentLocation != agentStart:
        
        playerContinue = ""  

        while playerContinue.lower() != "c":
            playerContinue = input("Type 'c' to see the next choice for the agent: ")

        printWorld(worldMap, currentLocation)

        possibleMovesBack = []

        for key, value in possibleMoves.items():

            newX, newY = currentLocation[1] + value[1], currentLocation[0] + value[0]

            if [newY, newX] in unSafeSpots:
                continue
            
            possibleMovesBack.append([newY, newX])
        
        minDistance = float('inf')
        minDistanceMove = 0

        for i in range(len(possibleMovesBack)):
            distanceToEnd = distance(possibleMovesBack[i], agentStart)
            
            if distanceToEnd < minDistance:
                minDistance = distanceToEnd
                minDistanceMove = possibleMovesBack[i]
        
        currentLocation = minDistanceMove

        playerLocationUpdate(currentLocation)
    
    playerContinue = ""

    while playerContinue.lower() != "c":
            playerContinue = input("Type 'c' to see the next choice for the agent: ")

    printWorld(worldMap, currentLocation)
    
    print("THE AGENT HAS MADE IT'S WAY BACK...")
    print("SUCCESS!!")

#Calling main
main()