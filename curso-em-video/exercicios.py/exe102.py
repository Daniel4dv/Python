def fatorial(numero,show):
    if show:
        print('Processo de fatorial')
        print(f'numero escolhido: {numero}')
        i = numero
        while i >0:
            print(f'{i} x',end=' ')
            i-=1
        print()
        for i in range(numero-1,0,-1):
            print(f'{numero}x{i} = ',end='')
            numero *= i
            print(numero)
            print()
    else:
        for i in range(numero-1,0,-1):
            numero *= i
        print(numero)


fatorial(5,1)

