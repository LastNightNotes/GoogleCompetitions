for tc in range(int(input())):
    n = int(input())
    walk = []
    if n <= 30: # we walk only through 1st columns upto 30 rows
        walk = [(r,1) for r in range(1, n+1)]
    else: # we will walk 30 rows with some full rows
        n -= 30 # 1 for each row
        walkFull = []
        for i in range(30, 0, -1):
            rowSum = 2**i - 1    # 1 is subtracted because we have already subtracted 30 for 30 rows
            if n >= rowSum:
                walkFull.append(i+1) # here next row is added because power of 2 starts from 0
                n -= rowSum
        extra = n
        # walk
        c = 1
        walk.append((1,1))
        for r in range(2,31):
            if r in walkFull: # fully walk the r-th row
                if c == 1: # go right
                    for c in range(1, r+1): walk.append((r, c))
                else: # go left
                    for c in range(r, 0, -1): walk.append((r, c))
            else: walk.append((r,c))
            if c == r: c += 1
        # if there is extra even after completing 30 rows
        r += 1
        for e in range(extra):
            walk.append((r,c))
            if c == r: c += 1
            r += 1
    print('Case #{}: {}'.format(tc+1,"\n" + "\n".join(" ".join(map(str,p)) for p in walk)))