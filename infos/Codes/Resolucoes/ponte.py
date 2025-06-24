N = int(input())
adj = [[] for _ in range(N)]

for _ in range(N):
    u = int(input())
    vizinhos = list(map(int, input().split()))
    for v in vizinhos:
        adj[u].append(v)

time = 0
disc = [-1] * N
low = [-1] * N
parent = [-1] * N
pontes = 0

def dfs(u):
    global time, pontes
    time += 1
    disc[u] = time
    low[u] = time
    for v in adj[u]:
        if disc[v] == -1:
            parent[v] = u
            dfs(v)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                pontes += 1
        elif v != parent[u]:
            low[u] = min(low[u], disc[v])

for i in range(N):
    if disc[i] == -1:
        dfs(i)

print(pontes)
