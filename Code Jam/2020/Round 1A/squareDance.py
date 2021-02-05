def eliminate(i,j):
    alive[i][j] = False
    for h in [0,2]:
        i1,j1 = cn[i][j][h]
        i2,j2 = cn[i][j][h+1]
        if i1 != -1: cn[i1][j1][h+1] = (i2,j2); candidates.append((i1,j1)) # assign eliminating candidate' upper neighbour as the upper neighbour of eliminating candidate' bottom neighbour 
        if i2 != -1: cn[i2][j2][h] = (i1,j1); candidates.append((i2,j2))# bottom neighbour as bottom neigbour of upper neighbour

def wouldEliminate(i,j):
    s = [matrix[a][b] for a,b in cn[i][j] if a != -1]
    return s and matrix[i][j] < (sum(s)/len(s))

def getCN(i,j):
    t = [(-1,-1)]*4
    if i: t[0] = (i-1,j)
    if i != r-1: t[1] = (i+1,j)
    if j: t[2] = (i,j-1)
    if j != c-1: t[3] = (i,j+1)
    return t

inp = lambda: map(int, input().split())
for tc in range(int(input())):
    r, c = inp()
    matrix = [list(inp()) for i in range(r)]
    candidates = [(i,j) for j in range(c)  for i in range(r)]
    skill = sum(map(sum,matrix))
    alive = [[True]*c for i in range(r)]
    cn = [[getCN(i,j) for j in range(c)] for i in range(r)] # compass neighbours, 0=U, 1=D, 2=L, 3=R
 
    iLevel = 0
    while candidates:
        iLevel += skill
        toEliminate = [(i,j) for i,j in candidates if alive[i][j] and wouldEliminate(i,j)]
        candidates = []
        for i,j in toEliminate: eliminate(i,j) # we put remained candidates in eliminate funtion
        candidates = list(set(candidates))
        skill -= sum(matrix[i][j] for i,j in toEliminate)
    print('Case #{}: {}'.format(tc+1, iLevel ))# 0.026