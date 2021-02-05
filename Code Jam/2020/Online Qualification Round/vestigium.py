def myMethod():
    noOFrepeatedRows = 0
    for row in matrix:
        rowRepeated = False
        for item in row:
            if row.count(item) > 1:
                rowRepeated = True
                break
        if rowRepeated:
            noOFrepeatedRows += 1
    matrixTranspose = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(matrix[j][i])
        matrixTranspose.append(row)
    
    noOFrepeatedColumns = 0
    for row in matrixTranspose:
        columnRepeated = False
        for item in row:
            if row.count(item) > 1:
                columnRepeated = True
                break
        if columnRepeated:
            noOFrepeatedColumns += 1
    print('Case #{}: {} {} {}'.format(tc+1, trace, noOFrepeatedRows,noOFrepeatedColumns ))

def bestMethod():
    repeatedRows = [0] * size
    repeatedColumns = [0] * size
    for i in range(size):
        for j in range(size):
            for k in range(j+1,size):
                # print(i,j,k)
                if matrix[i][k] == matrix[i][j]: # check a cell with other cells in its row
                    repeatedRows[i] = 1   # apply current row as 1 means repeated
                if matrix[k][i] == matrix[j][i]: # check a cell with other cells in its column
                    repeatedColumns[i] = 1 # apply current column as 1 means repeated
    print('Case #{}: {} {} {}'.format(tc+1, trace, sum(repeatedRows),sum(repeatedColumns) ))

for tc in range(int(input())):
    size = int(input())
    matrix = []
    trace = 0
    for i in range(size):
        row = list(map(int, input().split(" ")))
        trace += row[i]
        matrix.append(row)
    # myMethod()
    bestMethod()

    