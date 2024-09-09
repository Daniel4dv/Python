def fatorial(numero,show=0):
    f = 1
    if show:
        print('=-'*20)
        print(f'{"Processo de fatorial":^40}')
        print('=-'*20)
        print()
        print(f'NÚMERO ESCOLHIDO]: {numero}')
        print()
        i = numero
        while i >0:
            if i >1:
                print(f'{i} x',end=' ')
                i-=1
            else:
                print(f'{i}',end=' = ?')
                i-=1         
        print()
        print()
        for i in range(numero,0,-1):
            print(f'{numero}x{i} = ',end='')
            f *= i
            print(f)
            print()
    else:
        for i in range(numero,0,-1):
            f *= i
        print(f)


fatorial(5,0)

