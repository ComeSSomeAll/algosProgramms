def leftBinSearch(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] >= key:
            right = middle
        else:
            left = middle
    if right < len(A) and A[right] == key:
        return right
    else:
        return -2

def rightBinSearch(A, key):
    left = -1
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] > key:
            right = middle
        else:
            left = middle
    if leftBinSearch(A,key) == -2:
        return -1
    else:
        return right

fin = open("binsearch.in")
fout = open("binsearch.out", "w")
N = int(fin.readline())
array = list(fin.readline().split())
for i in range(N):
    array[i] = int(array[i])
countOfKeys = int(fin.readline())
Keys = list(fin.readline().split())
for j in range(countOfKeys):
    Keys[j] = int(Keys[j])
for j in range(countOfKeys):
    print(leftBinSearch(array, Keys[j]) + 1, rightBinSearch(array, Keys[j]), file = fout)
fout.close()
