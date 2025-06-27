# Lê o número de vértices do grafo
N = int(input())

# Inicializa a lista de adjacência: cada vértice terá uma lista com seus vizinhos
adj = [[] for _ in range(N)]

# Lê a lista de adjacência para cada vértice
for _ in range(N):
    u = int(input())  # Vértice atual
    vizinhos = list(map(int, input().split()))  # Vizinhos do vértice atual
    for v in vizinhos:
        adj[u].append(v)  # Adiciona cada vizinho à lista de adjacência de u

# Inicializa variáveis globais para o algoritmo de Tarjan
time = 0          # Contador global de tempo de descoberta
disc = [-1] * N   # Tempo de descoberta de cada vértice (-1 significa não visitado)
low = [-1] * N    # Menor tempo de descoberta alcançável a partir de cada vértice
parent = [-1] * N # Pai de cada vértice na árvore DFS
pontes = 0        # Contador de pontes encontradas no grafo

# Função DFS para encontrar pontes
def dfs(u):
    global time, pontes

    # Marca o tempo de descoberta do vértice u
    time += 1
    disc[u] = time
    low[u] = time  # Inicialmente, o menor tempo é o próprio

    # Visita todos os vizinhos de u
    for v in adj[u]:
        if disc[v] == -1:
            # Se o vizinho ainda não foi visitado
            parent[v] = u  # Define o pai de v
            dfs(v)  # Chamada recursiva para v

            # Após visitar v, atualiza low[u]
            low[u] = min(low[u], low[v])

            # Verifica se a aresta (u, v) é uma ponte
            if low[v] > disc[u]:
                pontes += 1
        elif v != parent[u]:
            # Se v já foi visitado e não é o pai de u,
            # significa que existe uma back edge
            low[u] = min(low[u], disc[v])

# Executa DFS para todos os vértices, garantindo que todos os componentes sejam visitados
for i in range(N):
    if disc[i] == -1:
        dfs(i)

# Imprime o número de pontes encontradas
print(pontes)
