# for tc in range(int(input())):
#     rows, columns = list(map(int, input().split(" ")))
for tc in range(1):
    rows, columns = [4,3]
    output = "IMPOSSIBLE"
    possibleSolution = []
    for r in range(1,rows+1):
            for c in range(1,columns+1):
                possibleSolution.append((r,c))
    for ps in possibleSolution:
        path = [ps]
        last = ps
        
        while len(path) <= len(possibleSolution):
            # print(path)
            isAdded = False
            for ps in possibleSolution:
                if ps not in path:
                    if ps[0] != last[0] and ps[1] != last[1] and (ps[0]+ps[1]) != (last[0] + last[1]) and (ps[0]-ps[1]) != (last[0] - last[1]):
                        last = ps
                        isAdded = True
                        path.append(ps)
            if not isAdded:
                break
        if len(path) == len(possibleSolution):
            
            output = "POSSIBLE"
            for p in path:
                output += "\n" + str(p[0]) + " " + str(p[1])
            break
    print('Case #{}: {}'.format(tc+1, output ))
    # 4,3