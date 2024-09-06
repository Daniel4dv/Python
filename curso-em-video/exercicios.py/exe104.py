def validador_inteiro(n=0):
    while True:
        n = input('Digite um numero inteiro: ')
        try:
            n = int(n)
            break
        except ValueError:
            print('Este valor não é inteiro, Tente novamente')
    return n 


idade = validador_inteiro()
print(f'Idade: {idade}')


    




    