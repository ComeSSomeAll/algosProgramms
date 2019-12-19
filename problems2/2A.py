fin = open("sort.in")
fout = open("sort.out", "w")
a = int(fin.readline())
N = list(fin.readline().split())
for x in range(a):
    N[x] = int(N[x])


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


mergeSort(N)
for x in range(a):
    print(N[x], end=" ", file=fout)
fout.close()
