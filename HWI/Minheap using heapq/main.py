import heapq
q = [7, 8, 5, 9, 3, 2, 1, 0]
a = []
for i in q:
    heapq.heappush(a, i)
print(a)
print(heapq.heappop(a)) # heappop(q) - prints 7 coz its the 1st element
print(heapq.heappop(a))
# heap helps to sort elements (dynamically)