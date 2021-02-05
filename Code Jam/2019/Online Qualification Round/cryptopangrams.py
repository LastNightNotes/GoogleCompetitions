from math import gcd
for tc in range(int(input())):
    N, L = map(int, input().split(" "))
    c = list(map(int, input().split(" ")))
    i = next(i for i, k in enumerate(c) if k != c[0])
    g = gcd(c[0], c[i])
    p = (i + 1) % 2 * [g] + (i + 1) // 2 * [c[0] // g, g]
    for k in c[i:]:
        g = k // g
        p.append(g)
    sortedP = sorted(set(p))
    output = "".join([chr(ord('A') + sortedP.index(j)) for j in p])
    print('Case #{}: {}'.format(tc+1, output))