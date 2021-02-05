def permute(a, l, r, perm):
    if l == r:
        new = []
        new.extend(a)
        perm.append(new)
    else:
        for i in range(l ,r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1,r, perm)
            a[l], a[i] = a[i], a[l]
    return perm

trace = 2
size = 2
start = (trace - size) // size
matrix = []
print(matrix )
matrix[0][1] = 7
print(matrix )
for i in range(size):
    for j in range(size):
        
        matrix[i][j] = (start - i + j) % size + 1
print(matrix)

