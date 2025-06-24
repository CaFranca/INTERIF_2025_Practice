#Exemplo de entrada
''' import sys
from io import StringIO

entrada = """3
4
Beatriz
7.12
6.54 I
7.34
0.0 I
Isabel
3.45 I
7.12
7.52
5.67
Alice
0.0 I
7.59 I
0.0
7.12 I
"""  # cole aqui a entrada de múltiplas linhas do PDF

sys.stdin = StringIO(entrada) '''


#O código funciona, mas rápido definitivamente não é. Essa é uma implementação legível, mas não necessariamente boa.
#Não precisa armazenar todos, ou seja, é só fazer o loop for, em m, e ir atualizando o maior salto conforme.

num_competidores = int(input())
num_saltos = int(input())

lista_competidores_e_pulos = []
for i in range(num_competidores):
    lista_saltos = []
    nome = input()
    for m in range(num_saltos):
        possivel_salto = input()
        if not("I" in possivel_salto):
            lista_saltos.append(float(possivel_salto))
    lista_final = [nome, lista_saltos]
    lista_competidores_e_pulos.append(lista_final)

maximo = 0
maximo_nome = ""

for competidor in lista_competidores_e_pulos:
    maximo_competidor = max(competidor[1])
    if maximo_competidor > maximo:
        maximo = maximo_competidor
        maximo_nome = competidor[0]

print(maximo_nome)
print(maximo)
