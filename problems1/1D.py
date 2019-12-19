fin = open("smallsort.in")
fout = open("smallsort.out", "w")
a = int(fin.readline())
N = list(fin.readline().split())
for x in range(len(N)):
    N[x] = int(N[x])
j = 1
for x in range(a):
    for j in range(a):
        if N[x] <= N[j]:
            t = N[x]
            N[x] = N[j]
            N[j] = t    #N[x], N[j] = N[j], N[x]
for x in range(a):
    print(N[x], end = " ", file=fout)
fout.close()
