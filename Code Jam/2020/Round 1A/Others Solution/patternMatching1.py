input = lambda: __import__('sys').stdin.readline().rstrip()
MIS = lambda: map(int,input().split())

#######################

def word_without_asterisk(L):
    for w in L:
        if "*" not in w: return w

import re
def match(pattern, w):
    return bool(re.match("^"+pattern.replace("*", ".*")+"$", w))

def last_asterisk(w):
    for i in range(len(w)-1, -1, -1):
        if w[i] == "*": return i

def process():
    n = int(input())
    start = ""
    end = ""
    word = [input() for i in range(n)]
    midwords = []
    if any("*" not in w for w in word):
        w = word_without_asterisk(word)
        if all(match(p,w) for p in word): print(w)
        else: print("*")
        return
    for w in word:
        first = w.find("*")
        last = last_asterisk(w)
        nst = w[:first]
        nend = w[last+1:]
        if not (start.startswith(nst) or nst.startswith(start)): return print("*")
        if not (end.endswith(nend) or nend.endswith(end)): return print("*")
        if len(start) < len(nst): start = nst
        if len(end) < len(nend): end = nend
        midwords.append(w[first:last+1].replace("*",""))
    print(start + (''.join(midwords)) + end)

#######################

for TEST in range(int(input())):
    print("Case #{}: ".format(TEST+1), end='')
    process()