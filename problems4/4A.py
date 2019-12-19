fin = open("stack.in")
fout = open("stack.out", "w")
commandCount = int(fin.readline())
commandList = []
resultList = []
delList = []
j=0
for i in range(commandCount):
    commandList.append(0)
    commandList[i] = list(fin.readline().split())
    if commandList[i][0] == "+":
        resultList.append(commandList[i][1])
    else:
        delList.append(0)
        delList[j] = resultList.pop()
        j+=1
for i in range(len(delList)):
    print(delList[i], file=fout)
fout.close()