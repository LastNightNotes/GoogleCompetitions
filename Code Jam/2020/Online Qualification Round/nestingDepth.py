def myMethod(S):
    S = list(map(int, list(S)))
    newS = ""
    for index, i in enumerate(S):
        if index != 0 and i != 0 and S[index - 1] != 0:
            if i <= S[index - 1]:
                newS = newS[0:len(newS)-i]
            elif i > S[index - 1]:
                newS = newS[0:len(newS) - S[index - 1]]
                newS += "("*abs(i-S[index - 1])
        else:
            newS += "("*i 
        newS += str(i) + ")"*i 
    print('Case #{}: {}'.format(tc+1, newS ))

def otherMethod(S):
    opened = 0
    S += '0'
    print("Case #"+str(tc+1)+':',end = ' ')
    for i in range(len(S)):
        while(opened < int(S[i])):
            print('(',end = '')
            opened += 1
        while(opened > int(S[i])):
            print(')',end = '')
            opened -= 1
        if i!=len(S) - 1:
            print(S[i],end='')
    print()

for tc in range(int(input())):
    S = input()
    myMethod(S)
    # otherMethod(S)