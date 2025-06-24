# Entrada das distâncias
a = float(input())
b = float(input())
c = float(input())

maior = max(a, b, c)

quantos_empataram = [a, b, c].count(maior)

if quantos_empataram > 1:
    print("Empatou")
else:
    if maior == a:
        print("Equipe A ganhou")
    elif maior == b:
        print("Equipe B ganhou")
    else:
        print("Equipe C ganhou")
