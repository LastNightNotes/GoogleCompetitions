for tc in range(int(input())):
    N, D = map(int, input().split())
    angles = list(map(int, input().split()))
    minimum = D - 1

    if len(angles) != 1:
        possible = False
        for angle in angles:
            if angles.count(angle) >= D:
                minimum = 0
                possible = True
                break
        if not possible:
            for angle in angles:
                if angles.count(angle) == D - 1 and N >= D and angle < max(angles):
                    minimum = 1
                    possible = True
                    break
        if not possible:
            if D == 2:
                minimum = 1
            else:
                possible = False
                for i in angles:
                    for angle in angles:
                        if angle / i == D - 1:
                            minimum = angle / i - 1
                            possible = True
                            break
                    if possible: break
    print('Case #{}: {}'.format(tc+1, int(minimum)))