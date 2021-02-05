for tc in range(int(input())):
    x, y = map(int, input().split())
    N = 1
    E = 1
    S = -1
    W = -1
    search = True
    i = 0

    a = 0
    b = 0
    answer = ""
    while search:
        if x % 2 != 0 and y % 2 != 0:
            answer = "IMPOSSIBLE"
            break
        if x % 2 == 0 and y % 2 == 0:
            answer = "IMPOSSIBLE"
            break
        if x > 0:
            if y == 2:
                answer += "E"
        elif x < 0:
            answer += "W"
        if y > 0:
            answer += "N"
        elif y < 0:
            answer += "S"
        search = False
    print(answer)
    print('Case #{}: {}'.format(tc+1, answer))