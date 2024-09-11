import moeda
wallet = float(50)

print(f'Saldo: {wallet}')
while True:
    print('What do you wanna do?')
    print('1 - Increase')
    print('2 - Decrease')
    print('3 - Twice more')
    print('4 - get half')
    r = int(input('>'))
    if r == 1:
        wallet = moeda.aumentar(wallet)
        print('Balance increased!')
        print(wallet)
    elif r == 2:
        wallet = moeda.diminuir(wallet)
        print('Balance decreased!')
        print(wallet)
    elif r == 3:
        wallet = moeda.dobro(wallet)
        print('Balance twiced!')
        print(wallet)
    elif r == 4:
        wallet = moeda.metade(wallet)
        print('Balance halfed!')
        print(wallet)
    else:
        print('Opção inválida!')
        