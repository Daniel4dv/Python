jogador = {}
time = []
gols = []
while True: 

    jogador['nome'] = str(input('Nome do Jogador: '))
    while True:
        partidas = input('Quantas partidas ele jogou: ')
        if partidas.isdigit():
            partidas = int(partidas)
            jogador['partidas'] = partidas
            break
        else:
            print('Valor inválido, digite um número inteiro')
        
    gols.clear()
    for g in range(jogador['partidas']):
        while True:
            gol = (input(f'Quantos gols ele fez na partida {g+1}: '))
            if gol.isdigit():
                gol=int(gol)
                gols.append(gol)
                break
            else:
                print('Valor inválido, digite um número inteiro')
        
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    time.append(jogador.copy())

    while True:
        r = (input('Deseja continuar? \n'
                        '1 - sim \n'
                        '2 - Não \n'))
        if r.isdigit():
            r = int(r)
            if r==2 or r==1:
                break
            else:
                print('Erro! Opção inválida')
        else:
            print('Erro! Digite um valor válido')
    if r==2:
        break

# print(F'{"NOME":<10}  {"PARTIDAS":^2}  {"GOLS":^10}  {"TOTAL":>2}')
print('Cod',end='  ')
for c in jogador.keys():
    print(f'{c:<15}',end='')

print()
print('_'*60)
print()
for i,j in enumerate(time):
    print(f'{i+1:>4}  ',end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('_'*60)

while True:
    print()
    print('---LEVANTAMENTO DE DADOS---')
    while True:
        d = input("Deseja consultar os dados de qual jopgador? [0 - encerrar]")
        if d.isdigit():
            d = int(d)
            if d> (len(time)+1) or d<0:
                print('Valor inválido. Digite um codigo cadastrado')
            else:
                break
        else:
            print('Valor inválido. Tente novamente!')
    if d==0:
        print("Programa encerrado! VOLTE SEMPRE")
        break
    print(time[d-1])
    print('=-'*20)
    print(f'Partidas jogadas do {time[d-1]["nome"]}')
    for c in range(time[d-1]['partidas']):
        print(f'No jogo {c+1} fez {time[d-1]["gols"][c]} gols.')
    print('=-'*20)


