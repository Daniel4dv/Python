def ficha(nome ='Não cadastrado',gols=0):
    print('=-'*20)
    print('Cadastro')
    print(f'Nome: {nome}')
    print(f'Gols: {gols}')
    print('=-'*20)

while True:
    nome = input('Nome do jogador: ')
    gols = input('Gols: ')
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        ficha(gols = gols)
    else:
        ficha(nome,gols)


    

