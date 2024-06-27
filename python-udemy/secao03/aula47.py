nome   = input("Digite seu nome:")
idade  = input('Digite sua idade:')

if (nome and idade):
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'Seu nome invertido é {nome[::-1]}')  #INVERTENDO A STRING
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Digite os dados para fazer a verificação')
