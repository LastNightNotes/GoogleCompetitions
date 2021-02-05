from itertools import permutations 
def getList():
    return [i for i in range(1, size+1)]

def findRow(p): 
    row = []
    row.append(p)
    for i in list(permutations(getList())):
        canInsert = True
        for j in row:
            for k in range(size):
                if j[k] == i[k]:
                    canInsert = False
                    break
            if not canInsert:
                break
        if canInsert:
            row.append(i)
    return row

def getAnsText(m):
    output = "POSSIBLE"
    for row in m:
        output += "\n" + " ".join(map(str, row))
    return output

def find(p):
    output = "IMPOSSIBLE"
    for s in list(permutations(findRow(p))):
        if sum(s[i][i] for i in range(size)) == trace:
            output = getAnsText(s)
            break
    return output

for tc in range(int(input())):
    size, trace = list(map(int, input().split(" ")))
    output = "IMPOSSIBLE"

    if size == trace or trace == size*size:
        start = (trace - size) // size
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append((start - i + j) % size + 1)
            matrix.append(row)
        output = getAnsText(matrix)
    elif trace != size + 1 and trace != size*size - 1: # procede only if both these conditions are false
        for p in list(permutations(getList())):
            result = find(p)
            if "POSSIBLE" in result:
                output = result
                break
    print('Case #{}: {}'.format(tc+1, output ))