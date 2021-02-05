for tc in range(int(input())):
    n, k, p = map(int, input().split())
    stacks = [list(map(int, input().split())) for i in range(n)]
    s = [(i+1,j+1,stacks[i][j]) for j in range(k) for i in range(n)]
    s.sort(key=lambda x: x[2], reverse=True)
    t = []
    print(s)
    for i,j,k in s:
        if not p: break
        c = [(i,b) for b in range(1,j+1) if (i,b) not in t]
        if p >= len(c):
            t.extend(c)
            p -= len(c)
    bValue = sum([stacks[i-1][j-1] for i,j in t])
    print("Case #{}: {}".format(tc+1, bValue))