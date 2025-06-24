N = int(input())
M = int(input())

campeao = ""
melhor_salto = -1.0

for _ in range(N):
    nome_competidor = input().strip()
    for _ in range(M):
        salto = input().strip()
        if "I" not in salto:
            distancia = float(salto)
            if distancia > melhor_salto:
                melhor_salto = distancia
                campeao = nome_competidor

print(campeao)
print(f"{melhor_salto:.2f}")
