import random

fin = open("turtle.in")
fout = open("turtle.out", "w")
size = list(fin.readline().split())
h = int(size[0])  # строки #n
w = int(size[1])  # столбцы #m


def matr(N=1, M=1, a=0):
    sp = []
    if N != 1 and M == 1:
        M = N
    for i in range(N):
        sp.append([a] * M)
    return sp


matrix = []
matrixCopy = matr(h + 1, w + 1, 0)
matrixZero = matr(h + 1, w + 1, 0)
for i in range(h):
    matrix.append(list(fin.readline().split()))
for i in range(h):
    for j in range(w):
        matrix[i][j] = int(matrix[i][j])
for x in range(0, h):
    for y in range(1, w + 1):
        matrixCopy[x][y] = matrix[x][y - 1]
for x in range(0, h):
    for y in range(1, w + 1):
        matrixZero[x][y] = matrix[x][y - 1]
for i in range(h - 1, -1, -1):
    for j in range(1, w + 1):
        matrixCopy[i][j] = max(matrixCopy[i + 1][j], matrixCopy[i][j - 1]) + matrixZero[i][j]
print(matrixCopy[0][w], file=fout)
fout.close()

# для точки 2-1 проверерно, осталось для остальных проверить цикл!!