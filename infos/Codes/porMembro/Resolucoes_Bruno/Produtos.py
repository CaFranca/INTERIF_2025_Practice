#Provavelmente tem como melhorar muito, mas funciona. Levei uns 30-40 minutos para fazer. Este deve ser um dos exercícios mais tranquilos.

def get_primo(n_min, n_max):
    i = 2 #Começa por dois pq o módulo de todo número sobre um é zero
    num = n_min 
    while (num <= n_max): 
        if num % i == 0: #Ou seja, não é primo, caso não seja igual a ele mesmo
            if (i == num): #Se True, significa que o módulo vai ser 0. Se o número chegou até ele mesmo, significa que é primo.
                maior_primo = num #Pode ser que este não seja o maior número primo, mas, caso haja outro, ele irá substituir essa variável.
            num += 1 #Vai para o próximo número.
            i = 2 #"Reseta" o i para o começo. Começamos de baixo para cima para pegarmos múltiplos.
          
        else: #Ou seja, AQUELA divisão teve resto diferente de zero
            i += 1 #Tentamos com outro valor de i. Ex 9%2 = 1, mas 9%3 = 0.
          
    return maior_primo 

entrada = input().split()
print(get_primo(int(entrada[0]), int(entrada[1])))

#Nota: tem como melhorar sim, utilizando o algoritmo Crivo de Eratóstenes. Ele é mais rápido, mas a sintaxe é bem mais complexa. Não conseguiria implementar na olimpíada nem ferrando, pensando que existem outros exercícios.

