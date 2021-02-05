def easy_answer(n, k):
    print("Case #{}: POSSIBLE".format(q + 1))
    
    start = (k - n) // n
    ans = [0] * n
    for i in range(n):
        ans[i] = []
        for j in range(n):   
            ans[i].append((start - i + j) % n + 1)
    
    print_ans(ans)

def check_sum(matrix, k):
    n = len(matrix)
    trace = 0

    for i in range(n):
        trace += matrix[i][i]

    return trace == k

def check(a, k):
    n = len(a)
    for i in range(n):
        b = [0] * (n + 1)
        for j in range(n):
            b[a[i][j]] += 1
            if b[a[i][j]] == 2:
                return False
    for i in range(n):
        b = [0] * (n + 1)
        for j in range(n):
            b[a[j][i]] += 1
            if b[a[j][i]] == 2:
                return False
    return True and check_sum(a, k)

def print_ans(a):
    for i in a:
        print(' '.join([str(k) for k in i]))

def odd_2(n, k):
    if n == 3:
        print("Case #{}: IMPOSSIBLE".format(q + 1))
        return False
    if n % 2 == 1:
        dct = {}
        for i in range(n):
            dct[i] = i + 1
        if k == n * n - 2:
            dct[0] = n
            dct[1] = n - 1
            dct[n - 1] = 1
            dct[n - 2] = 2
        ans = [0] * n
        for i in range(n):
            ans[i] = [0] * n
        ans[0][0] = dct[1]
        ans[0][1] = dct[0]
        ans[1][0] = dct[0]
        ans[1][1] = dct[1]
        for i in range(2, n):
            ans[i][i] = dct[0]
            if i + 1 != n:
                ans[i][i + 1] = dct[1]
        ans[n - 1][2] = dct[1]
        start = 0
        for i in range(n - 1):
            now = start + 2
            for j in range(n):
                if not ans[i][j]:
                    ans[i][j] = dct[now]
                    now += 1
                    if now >= n:
                        now %= n
                        now += 2
            start -= 2
            start %= (n - 2)
        for j in range(n):
            if not ans[n - 1][j]:
                b = [0] * (n + 1)
                for i in range(n - 1):
                    b[ans[i][j]] = 1
                for i in range(1, n + 1):
                    if b[i] == 0:
                        ans[n - 1][j] = i
    print("Case #{}: POSSIBLE".format(q + 1))
    print_ans(ans)

def even_2(n, k):
    print("Case #{}: POSSIBLE".format(q + 1))
    dct = {}
    for i in range(n):
        dct[i] = i + 1
    if k == n * n - 2:
        dct[0] = n
        dct[1] = n - 1
        dct[n - 1] = 1
        dct[n - 2] = 2
    ans = [0] * n
    for i in range(n):
        ans[i] = [0] * n
    ans[0][0] = dct[1]
    ans[n - 1][n - 1] = dct[1]
    ans[n - 1][0] = dct[0]
    ans[0][n - 1] = dct[0]
    for i in range(1, n - 1):
        ans[i][i] = dct[0]
        ans[i][n - i - 1] = dct[1]
    for j in range(2, n):
        for i in range(n):
            if j % 2 == 1:
                ans[i][(i + j - 1) % n] = dct[j]
            else:
                ans[i][(j - i - 1) % n] = dct[j]
    print_ans(ans)

def odd_3(n, k):
    print("Case #{}: POSSIBLE".format(q + 1))
    a = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            x = k - (n - 2) * i - j
            if 0 < x < n and x != i and x != j and i != j:
                a = [i, j, x]
    ans = [0] * n
    for i in range(n):
        ans[i] = [0] * n
    ans[0][0] = a[1]
    ans[n - 1][n - 1] = a[2]
    ans[n - 1][0] = a[0]
    ans[0][n - 1] = a[0]
    for i in range(1, n):
        if i != n - 1:
            ans[i][i] = a[0]
        ans[i][i - 1] = a[1 + i % 2]
        ans[i - 1][i] = a[1 + i % 2]
    j = 1
    for i in range(1, n + 1):
        if i not in a:
            j += 1
            for ww in range(n):
                ans[ww][(j + ww) % n] = i
    print_ans(ans)

def union(mat1, mat2):
    ans = []
    for i in range(len(mat1)):
        ans.append(mat1[i] + mat2[i])

    return ans

def three_color(n):
    if n == 4:
        return [[1, 2, 3, 4], [3, 1, 4, 2], [4, 3, 2, 1], [2, 4, 1, 3]]
    if n % 2 == 1:
        ans = [[0 for i in range(n)] for j in range(n)]
        ans[0][0] = 2
        ans[n - 1][n - 1] = 3
        ans[0][n - 1] = ans[n - 1][0] = 1
        for i in range(1, n - 1):
            ans[i][i] = 1

        for i in range(0, n - 1, 2):
            ans[i][i + 1] = 3
            ans[i + 1][i] = 3

        for i in range(1, n - 1, 2):
            ans[i][i + 1] = 2
            ans[i + 1][i] = 2

        for x in range(2, n - 1):
            for i in range(0, n):
                if x + i >= n:
                    break
                ans[i][x + i] = x + 2
                ans[x + i][i] = n - x + 2

        return ans

    n = n // 2
    first = [[((j - i) % n) + 0 + 1 for i in range(n)] for j in range(n)]
    second = third = [[((j - i) % n) + n + 1 for i in range(n)] for j in range(n)]
    fourth = three_color(n)

    return union(first, second) + union(third, fourth)

def even_3(n, k):
    print("Case #{}: POSSIBLE".format(q + 1))
    a = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            x = k - (n - 2) * i - j
            if 0 < x < n and x != i and x != j and i != j:
                a = [i, j, x]
                break
    dct = {}

    dct[0] = a[0]
    dct[1] = a[1]
    dct[2] = a[2]
    x = [0] * (n + 1)
    x[a[0]] = 1
    x[a[1]] = 1
    x[a[2]] = 1
    now = 1
    for i in range(3, n):
        while (x[now] == 1):
            now += 1
        dct[i] = now
        x[now] = 1
    ans = three_color(n)
    for i in range(n):
        for j in range(n):
            ans[i][j] = dct[ans[i][j] - 1]
    print_ans(ans)

def game(q, n, k):
    if k == n or k == n * n:
        easy_answer(n, k)
    elif k == n + 1 or k == n * n - 1:
        print("Case #{}: IMPOSSIBLE".format(q + 1))
        return
    elif k == n + 2 or k == n * n - 2:
        if n % 2 == 1:
            odd_2(n, k)
        else:
            even_2(n, k)
    else:
        if n % 2 == 1:
            odd_3(n, k)
        else:
            if n != 4 or k != 10:
                even_3(n, k)
            else:
                print("Case #{}: POSSIBLE".format(q + 1))
                ans = [[2, 3, 1, 4], [3, 2, 4, 1], [1, 4, 3, 2], [4, 1, 2, 3]]
                print_ans(ans)

t = int(input())
q = 0

def game1(q):
    n,k = [int(x) for x in input().split()]
    game(q,n,k)

while t:
    t -= 1
    game1(q)
    q += 1
