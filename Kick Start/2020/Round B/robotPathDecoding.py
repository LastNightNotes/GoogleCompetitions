def findString(l):
    string = [i for i in l]
    start = []
    for i,char in enumerate(string):
        if char == "(":
            start.append(i+1)
        if char == ")":
            s = "".join(string[start[-1]:i])
            times = int(string[start[-1]-2])-1
            string.pop(i)
            index = start[-1] - 1
            string.pop(index)
            string.insert(index, s*times)
            string.pop(index-1)
            k = "".join(string)
            string.clear()
            start.clear()
            if "(" in k:
                return findString(k)
            else:
                return k
            break

for tc in range(int(input())):
    string = input()
   
    if "(" in string:
        string = findString(string)
    s = string.count("S")
    n = string.count("N")
    e = string.count("E")
    w = string.count("W")
    x = 1
    y = 1
    moveX = e - w
    moveY = s - n
    if moveX >= 0: x += moveX
    else: 
        x = 10**9
        x += moveX + 1
    if moveY >= 0: y += moveY
    else: 
        y = 10**9
        y += moveY + 1
    print("Case #{}: {} {}".format(tc+1, x,y))