for tc in range(int(input())):
    N = int(input())
    day = []
    for i in range(N):
        activity = {"index":i}
        activity["S"], activity["E"] = list(map(int, input().split(" ")))
        day.append(activity)
    day = sorted(day,  key=lambda x: x["S"])
    output = [" "]*N
    endC = 0
    endJ = 0
    for activity in day:
        if activity["S"] >= endJ:
            output[activity["index"]] = "J"
            endJ = activity["E"]
        elif activity["S"] >= endC:
            output[activity["index"]] = "C"
            endC = activity["E"]
        else:
            output = ["IMPOSSIBLE"]
            break
    print('Case #{}: {}'.format(tc+1, "".join(output) ))