n = int(input())
minutos_ = list(map(int, input().split()))

minutos_ = set(minutos_)

contador = 0
tempo_assistido = 0

for minuto in range(1, 91):
    tempo_assistido += 1
    if minuto in minutos_:
        contador = 0
    else:
        contador += 1
        if contador == 15:
            break

print(tempo_assistido)
