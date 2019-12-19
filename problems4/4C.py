fin = open("brackets.in")
fincopy = open("brackets.in")
fout = open("brackets.out", "w")

def is_correct_brackets(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')


    return not text
def countOfStrings():
    n = fincopy.readline()
    k = 0
    while n!= '':
        n = fincopy.readline()
        k+=1
    return k
k = countOfStrings()
stack = []
res = []
for i in range(k):
    stack.append(fin.readline())
stack = [line.rstrip('\n') for line in stack]
for i in range(k):
    if is_correct_brackets(stack[i]) == True:
        res.append("YES")
    else:
        res.append("NO")
    print(res[i],file=fout)
fout.close()