import climage

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
    



    