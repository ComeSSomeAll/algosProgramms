fin = open("inversions.in")
fout = open("inversions.out", "w")
a = int(fin.readline())
N = list(fin.readline().split())
for x in range(a):
    N[x] = int(N[x])

def merge_sort(arr, inv):
    if (len(arr) == 1): return 0
    if (len(arr) > 1):
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        a = merge_sort(L, inv)
        b = merge_sort(R, inv)
        count = 0

        i = 0
        j = 0
        k = 0
        r = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                r += 1
                i += 1
                k += 1

            else:  # R[j]<L[i]
                arr[k] = R[j]
                inv = inv + (len(L) - r)
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
        count = inv + a + b
        return count



inv = 0
m = 0
x = 0
result = merge_sort(N,inv)
print(result, end=" ", file=fout)
fout.close()