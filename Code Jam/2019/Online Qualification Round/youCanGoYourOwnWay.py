for tc in range(int(input())):
    size = int(input())
    P = input()
    # output = "".join(["E" if i == "S" else "S" for i in P]) # one way
    # output = "".join({"S": "E", "E": "S"}[c] for c in P)  # 2nd way
    output = P.replace("E","T").replace("S", "E").replace("T", "S")  # 3rd way
    print('Case #{}: {}'.format(tc+1, output))