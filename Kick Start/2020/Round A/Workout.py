import math
for tc in range(int(input())): # we have to create partitions of length as small as possible
    old, newLimit = map(int, input().split())
    minutes = list(map(int, input().split()))
    diff = [minutes[i+1] - minutes[i] for i in range(old - 1)]
    lb = 1 # lower bound
    ub = max(diff) # upper bound
    while lb < ub:
        mid = int((lb + ub)/2)
        if sum([(math.ceil(i / mid) - 1) for i in diff]) <= newLimit: 
            # means we can add new partitions having maximum partition width = mid
            ub = mid # now check if max partition length < mid is possible or not
        else: # means we cannot add new partitions having maximum partition width <= mid
            lb = mid + 1 # now check if max partition length > mid is possible or not
    print("Case #{}: {}".format(tc+1, lb))