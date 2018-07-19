import random

f1 = open('original.txt', 'r')
f2 = open('scrambled.txt', 'a')
s = f1.read()

def scramble(k):
    k = list(k)
    li = len(k)
    init = k[0]
    proc = ""
    m = li-1
    final = k[li-1]

    if li <= 3:
        return "".join(k)
    else:
        for v in range(li - 2):
            index = random.randint(1, (m - 1))
            proc = proc + k[index]
            k.pop(index)
            m -= 1
    return str(init+proc+final)

si = s.split(" ")

l = len(si)

for x in range(0, l):
    f1 = scramble(si[x])
    print f1
    f2.write(f)
    f2.write(" ")

f1.close()
f2.close()