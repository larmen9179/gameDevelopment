
map = [[1, 1, 1, 1, 1],
       [1, 0, 0, 0, 1],
       [1, 0, 1, 0, 1],
       [1, 0, 0, 0, 1],
       [1, 1, 1, 1, 1]]

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 1:
            print("|****|", end="")
        else:
            print("      ", end = "")
    
    print()
    print()


    