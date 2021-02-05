for tc in range(int(input())):
    n = int(input())
    checkpoints = list(map(int, input().split()))
    peak = 0
    for i in range(1,n-1):
        if  checkpoints[i+1] < checkpoints[i] > checkpoints[i-1]:
             peak += 1
    print("Case #{}: {}".format(tc+1, peak))