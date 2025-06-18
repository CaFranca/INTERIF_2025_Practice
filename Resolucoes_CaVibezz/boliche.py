# Número de jogadores que participarão
quantidade = int(input())

# Lista para armazenar os dados dos jogadores (nome, pontuação total e pontuação acumulada por frame)
jogadores = []

for _ in range(quantidade):
    nome = input().strip()
    jogadas = list(input().strip())  # lista de arremessos, ex: ['X', '3', '4', ...]

    indice_jogada = 0  # índice atual na lista de jogadas
    frame_atual = 0    # contador de frames (0 a 9)
    pontuacoes_acumuladas = []  # lista para pontuação acumulada por frame
    pontuacao_total = 0

    while frame_atual < 10:
        # Verifica se é strike (derrubou 10 pinos no primeiro arremesso)
        if jogadas[indice_jogada] == 'X':
            # Base do strike = 10
            soma_frame = 10

            # Soma os próximos dois arremessos para o bônus do strike
            if indice_jogada + 1 < len(jogadas):
                soma_frame += 10 if jogadas[indice_jogada + 1] == 'X' else int(jogadas[indice_jogada + 1])
            if indice_jogada + 2 < len(jogadas):
                soma_frame += 10 if jogadas[indice_jogada + 2] == 'X' else int(jogadas[indice_jogada + 2])

            indice_jogada += 1  # strike consome apenas um arremesso
        else:
            # Se não foi strike, pega os dois arremessos do frame
            primeira_jogada = int(jogadas[indice_jogada])
            segunda_jogada = int(jogadas[indice_jogada + 1])

            # Verifica se foi spare (derrubou os 10 pinos nos dois arremessos do frame)
            if primeira_jogada + segunda_jogada == 10:
                soma_frame = 10
                # Bônus do spare: soma do próximo arremesso
                if indice_jogada + 2 < len(jogadas):
                    soma_frame += 10 if jogadas[indice_jogada + 2] == 'X' else int(jogadas[indice_jogada + 2])
            else:
                # Pontuação normal (sem bônus)
                soma_frame = primeira_jogada + segunda_jogada

            indice_jogada += 2  # consumiu dois arremessos

        # Atualiza pontuação total e acumulada
        pontuacao_total += soma_frame
        pontuacoes_acumuladas.append(pontuacao_total)
        frame_atual += 1

    # Guarda os dados do jogador
    jogadores.append((pontuacao_total, nome, pontuacoes_acumuladas))

# Ordena lista de jogadores pela pontuação total (decrescente) e pelo nome (crescente) em caso de empate
jogadores.sort(key=lambda x: (-x[0], x[1]))

# Exibe o resultado formatado
for pontuacao_total, nome, acumulados in jogadores:
    resultado_frames = '|'.join(str(p) for p in acumulados)
    print(f"{nome} : |{resultado_frames}| Total = {pontuacao_total}")
