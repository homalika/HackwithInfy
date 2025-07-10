d = {3:1,2:2,1:3}
sd = sorted(d.items(), key = lambda x:x[1], reverse = True) # descending order
print(sd)
for i in range(len(sd)):
    print(sd[i][1]) # prints frqs
    print(sd[i][0]) # prints keys