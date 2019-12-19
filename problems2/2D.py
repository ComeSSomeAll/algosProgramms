fin = open("antiqs.in")
fout = open("antiqs.out", "w")
a = int(fin.readline())
array = []
for i in range(1,a+1):
    array.append(i)
for i in range(a):
    array[i],array[i//2] = array[i//2], array[i]
#key = (1 + a) // 2
#array[a - 1], array[key] = array[key], array[a - 1]
print(*array, end=" ", file=fout)
fout.close()
