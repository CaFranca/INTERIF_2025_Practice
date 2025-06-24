L, C = map(int, input().split())
N = int(input())

tab = [['*' for _ in range(C)] for _ in range(L)]

for _ in range(N):
    LF, CF = map(int, input().split())
    tab[LF-1][CF-1] = 'F'

LP, CP = map(int, input().split())
LP -= 1
CP -= 1
tab[LP][CP] = ' '

movimentos = input().strip()

direcoes = {
    'N': (-1, 0),
    'S': (1, 0),
    'L': (0, 1),
    'O': (0, -1)
}

pontuacao = 0

for m in movimentos:
    dL, dC = direcoes[m]
    nLP = LP + dL
    nCP = CP + dC

    if 0 <= nLP < L and 0 <= nCP < C:
        LP, CP = nLP, nCP

        if tab[LP][CP] == '*':
            pontuacao += 1
            tab[LP][CP] = ' '
        elif tab[LP][CP] == 'F':
            pontuacao = 0

print(pontuacao)
