T = int(input())
for z in range(1, T+1):
    N = int(input())
    pref = ""
    suff = ""
    mid = ""
    bad = False
    for i in range(N):
        strs = input().strip().split('*')
        if pref.startswith(strs[0]):
            pass
        elif strs[0].startswith(pref):
            pref = strs[0]
        else:
            bad = True
        if suff.endswith(strs[-1]):
            pass
        elif strs[-1].endswith(suff):
            suff = strs[-1]
        else:
            bad = True
        mid += "".join(strs[1:-1])
    print("Case #%d: %s" % (z, "*" if bad else \
        (pref + mid + suff)))
