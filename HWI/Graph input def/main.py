n, m = map(int, input().split())  # Read number of provinces and roads
graph = {i: [] for i in range(1, n+1)}  # Initialize adjacency list
print(graph)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # Because roads are bidirectional
print(graph)