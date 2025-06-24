fen = input().strip()

linhas = fen.split('/')

for linha in linhas:
    casas = []
    for c in linha:
        if c.isdigit():
            casas.extend([' '] * int(c))
        else:
            casas.append(c)
    print('|' + '|'.join(casas) + '|')
