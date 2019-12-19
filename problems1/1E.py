fin = open("sortland.in")
fout = open("sortland.out", "w")
a = int(fin.readline())
N = list(fin.readline().split())
for x in range(a):
    N[x] = float(N[x])
minValue = 1000001
maxValue = -1
minValue_i = 0
maxValue_i = 0
avrg_i = 0
for x in range(a-1):
    if N[x] < minValue:
        minValue = N[x]
        minValue_i = x+1
    if N[x] > maxValue:
        maxValue = N[x]
        maxValue_i = x+1
Ns = sorted(N)[len(N) // 2]
for x in range(a):
    if N[x] == Ns:
        avrg_i = x+1
print(minValue_i, "", avrg_i, "", maxValue_i,  file=fout)
fout.close()
