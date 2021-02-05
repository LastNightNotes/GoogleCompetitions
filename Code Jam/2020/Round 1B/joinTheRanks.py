for tc in range(int(input())):
    R, S = map(int, input().split())
    deck = []
    finalDeck = []
    result = []
    for i in range(1,S+1):
        for j in range(1,R+1):
            deck.append((j,i))
    print(deck)
    if R >= S:
        for i,j in zip(range(R, 1, -1), range(1, S+1) ):
            n  = deck.index((i,j))
            result.append((i, n))
            p = deck[n+1: n+1+i-1]
            for k in range(i-1):
                deck.pop(n+1)
            p.extend(deck)
            deck = []
            deck.extend(p)
    else:
        for i in range(R, 1, -1):
            for j in range(1, S):
                n  = deck.index((i,j))
                result.append((i, n+i+1-j))
                print(i,j,n)
                p = deck[n+1: n+i+i-j+1]
                print(p)
                for k in range(i+i-1):
                    deck.pop(n+1)
                p.extend(deck)
                deck = []
                deck.extend(p)
                print(deck)
    for i in range(1,R+1):
        for j in range(1,S+1):
            finalDeck.append((i,j))
    print(deck, finalDeck)
    answer = str(len(result))
    answer += "\n" + "\n".join(" ".join(map(str,p)) for p in result)
    print('Case #{}: {}'.format(tc+1, answer))