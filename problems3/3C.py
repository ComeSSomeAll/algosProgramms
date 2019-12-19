fin = open("isheap.in")
fout = open("isheap.out", "w")
N = int(fin.readline())
arr = list(fin.readline().split())
for i in range(N):
    arr[i] = int(arr[i])


def isHeap(arr, n):
    for i in range(int((n - 2) / 2) + 1):

        if arr[2 * i + 1] < arr[i]:
            return False

        if (2 * i + 2 > n and
                arr[2 * i + 2] < arr[i]):
            return False
    return True

varTest = isHeap(arr,N)
if varTest == False:
    print("NO", file=fout)
else:
    print("YES", file=fout)
fout.close()
