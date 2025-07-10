# arr = [1, 1, 1, 2, 2, 4, 4, 3]
dic = {1:3,2:2,3:1,4:2}
'''
print(dic)
my = list(dic.values())
my = sorted(my)
print(my)
for i in my:
    for k, v in dic.items():
        if v == i:
            print(k, v)  # prints dic by sorted frq (values) 
            del dic[k]
            break
'''
sd = sorted(dic.items(), key = lambda x : x[1])
d = dict(sd)
print(d)