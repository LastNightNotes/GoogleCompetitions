def rev(s):
    return "".join([s[i] for i in range(len(s)-1, -1,-1)])
    
for tc in range(int(input())):
    n = int(input())
    patterns = [input() for i in range(n)]
    myWord = ""
    end = []
    for p in patterns:
        if (p.index("*") == 0):
            end.append(p[1:])
    end.sort(key=lambda x: len(x))
    myWord = end[-1]
    m = rev(myWord)
    for i in end:
        try:
            if m.index(rev(i)) != 0:
                myWord = "*"
                break
        except ValueError:
            myWord = "*"
            break
    print('Case #{}: {}'.format(tc+1, myWord))
