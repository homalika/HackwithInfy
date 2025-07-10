n = 5
p = []
for i in range(1, n+1):
    t = []
    if i == 1:
        t.append(1)
    else:
        t.append(1)
        for j in range(1, i - 1):
            t.append(p[i - 2][j - 1] + p[i - 2][j])
        t.append(1)
    p.append(t)
for i in p:
    print(i)