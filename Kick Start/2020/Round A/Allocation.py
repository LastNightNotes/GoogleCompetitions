for tc in range(int(input())):
    n, b = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    housePucrhased = 0
    for i in range(n):
        if b < prices[i]: break
        b -= prices[i]
        housePucrhased += 1
    print("Case #{}: {}".format(tc+1, housePucrhased))