from sys import stdout
for tc in range(int(input())):
    n, b, f = map(int, input().split())
    k = min(b.bit_length() +1, f)
    queries = [(("0"*(1 << i) + "1"*(1 << i))*n)[:n] for i in range(k)]   # 1 << i creates 1,2, 4, 8 for i = 0,1,2,3
    responses = []
    for q in queries:
        print(q)
        stdout.flush()
        responses.append(input())
    query_it = zip(*queries)
    response_it = zip(*responses)
    response_col = next(response_it, None)
    broken = []
    for j, query_col in enumerate(query_it):
        if query_col == response_col: # (ith bits of every query) == (ith bits of every response)
            response_col = next(response_it, None)
        else:
            broken.append(j)
    print(*broken)
    stdout.flush()
    input()
    

