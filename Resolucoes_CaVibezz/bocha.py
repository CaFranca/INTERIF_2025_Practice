
a = float(input())
b = float(input())
c = float(input())


maior = max(a, b, c)


quantidade_maior = (a == maior) + (b == maior) + (c == maior)


if quantidade_maior > 1:
    print("Empatou")
else:
    if a == maior:
        print("Equipe A ganhou")
    elif b == maior:
        print("Equipe B ganhou")
    else:
        print("Equipe C ganhou")
