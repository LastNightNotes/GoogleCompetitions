import time
def getPrefixes(s):
    prefixes = []
    for string in s:
        prefixes.extend([string[:i+1] for i in range(len(string)) if string[:i+1] not in prefixes])
    return prefixes

def getIndexes(char):
    p = []
    for s in char:
        index = [i for i,st in enumerate(strings) if st.find(s) == 0]
        if (len(index) // k) == 0: continue
        p.append({"p" : s, "c" : len(s), "i" : index})
    return p

def getScore(p):
    score = 0
    indexes = []
    extend = indexes.extend
    for pre in p:
        pre["i"] = [i for i in pre["i"] if i not in indexes]
        extend(pre["i"])
        l = len(pre["i"])
        if l % k != 0:
            pre["i"] = pre["i"][:l - l%k]
        score += len(pre["p"])*(len(pre["i"]) // k)
    return score

for tc in range(int(input())):
    n, k = map(int, input().split())
    strings = [input() for i in range(n)]
    t = time.time()
    p = getIndexes(getPrefixes(strings))
    p.sort(key=lambda x: x["c"], reverse=True)
    score = getScore(p)
    print("%f" %(time.time() -t))
    print("Case #{}: {}".format(tc+1, score))