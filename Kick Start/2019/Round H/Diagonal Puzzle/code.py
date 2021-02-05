with open("input.txt", "r") as file:
    data = file.read().splitlines()

totalCases = int(data[0])
print(totalCases)
startFrom = 1
endPpoint = 0
myList = []
for i in range(totalCases):
    endPpoint = startFrom + int(data[startFrom])
    myList.append(data[startFrom+1:endPpoint+1])
    startFrom = endPpoint + 1 

def getParallelDiagonal(i, j, length):
    while i > -1 and j > -1:
        i -= 1
        j -= 1
    pdList = []
    if i == j:
        for k in range(length):
            pdList.append([k, k])
        return pdList
    else:
        while i < (length - 1) and j < (length - 1):
            i += 1
            j += 1
            pdList.append([i, j])
        return pdList

def getPerpendicularDiagonal(i, j, length):
    while i > -1 and j < length:
        i -= 1
        j += 1
    pdList = []
    while i < (length - 1) and j > 0:
        i += 1
        j -= 1
        pdList.append([i, j])
    return pdList

for grid in myList:
    move = 0
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    for i in range(len(grid)):
        for j, value in enumerate(grid[i]):
            if value == ".":
                parallelDiagonal = getParallelDiagonal(i, j, len(grid))
                parallelDiagonalElements = [grid[cell[0]][cell[1]] for cell in parallelDiagonal]
                if "#" in parallelDiagonalElements:
                    if parallelDiagonalElements.count("#") == 1:
                        rowIndex = parallelDiagonal[parallelDiagonalElements.index("#")][0]
                        colIndex = parallelDiagonal[parallelDiagonalElements.index("#")][1]
                        perpendicularDiagonal = getPerpendicularDiagonal(rowIndex, colIndex, len(grid)) 
                        perpendicularDiagonalElements = [grid[cell[0]][cell[1]] for cell in perpendicularDiagonal]
                        #"There is only 1 black"
                        if perpendicularDiagonalElements.count("#") == 1:
                            for c in parallelDiagonal:
                                grid[c[0]][c[1]] = "#"
                            for d in perpendicularDiagonal:
                                grid[d[0]][d[1]] = "#"
                            move += 2
                            #"This black in also only single in perpendicular diagonal")
                       
                else: # there are all white in the parallel diagonal of (i,j)
                    move += 1
                    for c in parallelDiagonal:
                        grid[c[0]][c[1]] = "#"
    allBlack = True
    for row in grid:
        print(row)
        if not allBlack:
            continue
        allBlack = "." not in row
    print("is done : ", allBlack)
    print("Case #", myList.index(grid) + 1, ":", move)
    

    
