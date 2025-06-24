def get_primo(n_min, n_max):
    maior_primo = -1
    for num in range(n_min, n_max + 1):
        if num < 2:
            continue
        i = 2
        primo = True
        while i * i <= num:
            if num % i == 0:
                primo = False
                break
            i += 1
        if primo:
            maior_primo = num
    return maior_primo

entrada = input().split()
print(get_primo(int(entrada[0]), int(entrada[1])))
