tamanho = 3

for i in range(tamanho):
    for j in range(1,tamanho+1):

        if j == tamanho - i:
            for b in range(tamanho, j-1, -1):
                print("#", end='')
            break
        print(" ", end='')


    print()