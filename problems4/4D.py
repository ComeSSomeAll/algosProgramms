import operator

fin = open("postfix.in")
fout = open("postfix.out", "w")

def opz(lst):
    st = []
    for w in lst:
        if w.isdigit():
            st.append(int(w))
            continue
        y = st.pop()
        x = st.pop()
        z = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x - y,
            '*': lambda x,y: x * y,
            '/': lambda x,y: x // y
        }[w](x, y)
        st.append(z)
    return st.pop()

expression = fin.readline().split()
print(opz(expression), file=fout)
fout.close()