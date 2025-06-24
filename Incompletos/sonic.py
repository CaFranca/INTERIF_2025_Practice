N, M, K = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for estrada in range(1, M + 1):
    I, J, C = map(int, input().split())
    adj[I].append((J, C, estrada))
    adj[J].append((I, C, estrada))

visitadas = [False] * (M + 1)
resultado = []
inicio = 1
achou = False

def dfs(cidade_atual, caminho, cor_anterior, estradas_usadas):
    global achou
    if achou:
        return
    if len(caminho) == M:
        if caminho and cor_anterior != caminho[0][1]:
            achou = True
            for e in caminho:
                resultado.append(e[2])
        return
    for (vizinho, cor, id_estrada) in adj[cidade_atual]:
        if not visitadas[id_estrada] and cor != cor_anterior:
            visitadas[id_estrada] = True
            dfs(vizinho, caminho + [(cidade_atual, cor, id_estrada)], cor, estradas_usadas + 1)
            visitadas[id_estrada] = False

dfs(inicio, [], -1, 0)

if not achou:
    print(-1)
else:
    print(inicio)
    print(" ".join(map(str, resultado)))
