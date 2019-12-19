from collections import deque
fin = open("queue.in")
fout = open("queue.out", "w")
commandCount = int(fin.readline())
commandList = []
resultList = deque()
delList = []
j=0
for i in range(commandCount):
    commandList.append(0)
    commandList[i] = list(fin.readline().split())
    if commandList[i][0] == "+":
        resultList.append(commandList[i][1])
    else:
        delList.append(0)
        delList[j] = resultList.popleft()
        print(delList[j],file=fout)
        j+=1
#for i in range(len(delList)):
#    print(delList[i], file=fout)
fout.close()