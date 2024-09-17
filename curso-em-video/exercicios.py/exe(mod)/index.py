from coin_utilities import moeda
from coin_utilities import data
import importlib
import os
wallet = data.validar('Qual o saldo atual da sua carteira: ')
porc = 0

importlib.reload(moeda)

moeda.cabecalho()

print(f'Saldo: {wallet}')
while True:
    print('What do you wanna do?')
    print('1 - Increase')
    print('2 - Decrease')
    print('3 - Twice more')
    print('4 - get half')
    print('5 - Decrease(%)')
    print('6 - Increase(%)')
    print('7 - solve formatation (R$) ')
    r = int(input('>'))
    if r == 1:
        os.system('cls')
        moeda.cabecalho()
        wallet = moeda.aumentar(wallet)
        print('\033[92mBalance increased!\033[0m')
        print(wallet)
    elif r == 2:
        os.system('cls')
        moeda.cabecalho()
        wallet = moeda.diminuir(wallet)
        print('\033[91mBalance Decreased!\033[0m')
        print(wallet)
    elif r == 3:
        os.system('cls')
        moeda.cabecalho()
        wallet = moeda.dobro(wallet)
        print('\033[92mBalance twiced!\033[0m')
        print(wallet)
    elif r == 4:
        os.system('cls')
        moeda.cabecalho()
        wallet = moeda.metade(wallet)
        print('\033[91mBalance halved!\033[0m')
        print(wallet)

    elif r == 5:
       porc = data.validar('Decrease (%): ')
       wallet = moeda.tax(wallet,porc,r)
       os.system('cls')
       moeda.cabecalho()
       print(f'\033[91m{porc}% decreased!\033[0m')
       print(moeda.moeda(wallet))

    elif r == 6:
       porc = data.validar('Increase(%): ')
       wallet = moeda.tax(wallet,porc,r)
       os.system('cls')
       moeda.cabecalho()
       print(f'\033[92m{porc}% Increased!\033[0m')
       print(moeda.moeda(wallet))

    elif r==7:
        os.system('cls')
        moeda.cabecalho()
        print(moeda.moeda(wallet))     
    else:
        print('invalid option!')
        