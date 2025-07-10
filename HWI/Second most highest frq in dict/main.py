d = {1:3,2:2,3:1,4:5,5:5,6:7}
# sd = sorted(dic.items(), key = lambda x : x[1])
v = []
for i in d:
    v.append(d[i])
v = sorted(v)
print(v)
for k, j in d.items():
    if j == v[-2]:
        print(k)