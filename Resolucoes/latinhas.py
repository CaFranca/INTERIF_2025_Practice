vencedores = []
while True:
    N = int(input())
    if N == 0:
        break

    pontuacoes = []
    for _ in range(N):
        pontuacoes.append(int(input()))

    maior_valor = max(pontuacoes)
    sala_vencedora = pontuacoes.index(maior_valor) + 1
    vencedores.append(sala_vencedora)

for sala in vencedores:
    print(sala)
