tamanho = 0
while True:
    entrada = input()
    if entrada.isnumeric():
        tamanho = int(entrada)
        if 1 <= int(tamanho) <=8:
            break


for i in range(tamanho):
    for j in range(1,tamanho+1):
        # print('j', j)
        # print('t', tamanho-i)
        if j == tamanho - i:
            for b in range(tamanho, j-1, -1):
                print("#", end='')
            break
        print(" ", end='')
    print("  ", end='')
    for g in range(tamanho,0, -1):
        # print('j', j)
        # print('t', tamanho-i)
        if g == tamanho - i:
            for b in range(j-1,tamanho):
                print("#", end='')
    print("", end='')
    print()

