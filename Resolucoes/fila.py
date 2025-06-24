fila_prioritarios = []
fila_normal = []

while True:
    try:
        operacao = input().strip()
    except EOFError:
        break

    if operacao.startswith("CHEGADA"):
        _, nome, idade_str = operacao.split()
        idade = int(idade_str)
        if idade > 54:
            fila_prioritarios.append(nome)
        else:
            fila_normal.append(nome)
    elif operacao == "ATENDIMENTO":
        if fila_prioritarios:
            print(fila_prioritarios.pop(0))
        elif fila_normal:
            print(fila_normal.pop(0))
        else:
            break
