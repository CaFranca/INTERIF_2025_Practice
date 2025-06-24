X = int(input())
jogadores = []

for _ in range(X):
    nome = input().strip()
    lances = list(input().strip())
    
    pinos = []
    for lance in lances:
        if lance == 'X':
            pinos.append(10)
        else:
            pinos.append(int(lance))
    
    frame = 0
    i = 0
    acumulado = []
    total = 0
    
    while frame < 10:
        if pinos[i] == 10 and frame < 9:
            bonus = 0
            if i + 1 < len(pinos):
                bonus += pinos[i + 1]
            if i + 2 < len(pinos):
                bonus += pinos[i + 2]
            total += 10 + bonus
            acumulado.append(total)
            i += 1
            frame += 1
        elif frame < 9 and i + 1 < len(pinos) and pinos[i] + pinos[i + 1] == 10:
            bonus = 0
            if i + 2 < len(pinos):
                bonus = pinos[i + 2]
            total += 10 + bonus
            acumulado.append(total)
            i += 2
            frame += 1
        elif frame < 9:
            total += pinos[i] + pinos[i + 1]
            acumulado.append(total)
            i += 2
            frame += 1
        else:
            total += sum(pinos[i:])
            acumulado.append(total)
            frame += 1
    
    jogadores.append((total, nome, acumulado))

jogadores.sort(key=lambda x: (-x[0], x[1]))

for total, nome, frames in jogadores:
    linha = '|'.join(str(p) for p in frames)
    print(f"{nome} : |{linha}| Total = {total}")
