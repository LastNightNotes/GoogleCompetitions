for tc in range(int(input())):
    n, D = map(int, input().split())
    s = D
    X = list(map(int, input().split()))
    p = []
    for i in range(n-1,-1,-1 ):
        if  D % X[i] != 0:
            D -= D % X[i]
            p.append(D)
    if not p: p = [s]
    print("Case #{}: {}".format(tc+1, min(p)))