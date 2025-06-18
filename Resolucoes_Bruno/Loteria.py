lista_acertos = list(map(int, input().split()))
seis = cinco = quatro = 0

while(True):
    linha = input().split()
    if linha == ["0", "0", "0", "0", "0" ,"0"]:
        break
    jogador = list(map(int, linha))
    acertos = 0
    for i in range(6):
        if jogador[i] == lista_acertos[i]:
            acertos += 1
    if acertos == 6:
        seis += 1
    elif acertos == 5:
        cinco += 1
    elif acertos == 4:
        quatro += 1
        
print(f"6 {seis}")
print(f"5 {cinco}")
print(f"4 {quatro}")

#A melhora que dá para implementar é trocar a linha de if jogador[i] == lista_acertos[i] por acertos = sum(1 for a, b in zip(lista_acertos, linha) if a == b)
#Não precisa usar nem map nem list, pois posso ler elas como string mesmo, que não há problema.
