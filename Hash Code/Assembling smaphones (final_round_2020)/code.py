files = ["a_example.txt"]
for file in files:
    print(file)
    with open(file) as f:
        w, h, r, m, t, steps = map(int, f.readline().split())
        mounts = [list(map(int, f.readline().split())) for i in range(m)]
        tasks = []
        for i in range(t):
            task = {}
            task["score"], task["points_count"] = map(int, f.readline().split())
            points = list(map(int, f.readline().split()))
            task["points"] = []
            for j in range(task["points_count"]):
               task["points"].append([points[j*2], points[j*2+1]]) 
            task["capable_arms"] = []
            tasks.append(task)
        
        for a_index, arm in enumerate(mounts):
            for t_index,task in enumerate(tasks):
                pos = arm
                stepReq = 0
                canDo = True
                # ALSO ADD CHECK FOR WHETHER THERE THE PATH IS FREE
                # FROM MOUNT POINTS AND ARMS
                for p in task["points"]:
                    s = abs(p[0] - pos[0]) + abs(p[1] - pos[1])
                    # print(s)
                    stepReq += s
                    pos = p
                    if stepReq > steps:
                        canDo = False
                        break
                if canDo:
                    task["capable_arms"].append([a_index,stepReq])
                    if len(arm) < 3:
                        arm.append([])
                    arm[2].append([t_index, stepReq])
        print(w, h, r, m, t, steps,mounts, tasks)  
        