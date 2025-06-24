X, Y = map(int, input().split())
cadeiras = [list(map(int, input().split())) for _ in range(X)]

def vizinhos_ocupados(linha, cadeira):
    cont = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            novo_linha = linha + dx
            nova_cadeira = cadeira + dy
            if 0 <= novo_linha < X and 0 <= nova_cadeira < Y:
                if cadeiras[novo_linha][nova_cadeira] == 1:
                    cont += 1
    return cont

menor_vizinhos = 9
cadeiras_melhores = []

for fileira in range(X):
    for cadeira in range(Y):
        if cadeiras[fileira][cadeira] == 0:
            num_vizinhos = vizinhos_ocupados(fileira, cadeira)
            if num_vizinhos < menor_vizinhos:
                menor_vizinhos = num_vizinhos
                cadeiras_melhores = [fileira * Y + (cadeira + 1)]
            elif num_vizinhos == menor_vizinhos:
                cadeiras_melhores.append(fileira * Y + (cadeira + 1))

print(menor_vizinhos)
cadeiras_melhores.sort()
for c in cadeiras_melhores:
    print(c)
