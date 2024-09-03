jogador = {}
jogadores = []
gols = []
while True: 

    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input('Quantas partidas ele jogou: '))
    gols.clear()
    for g in range(jogador['partidas']):
        gol = int(input(f'Quantos gols ele fez na partida {g+1}: '))
        gols.append(gol)
    
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())

    r = int(input('Deseja continuar? \n'
                    '1 - sim \n'
                    '2 - Não \n'))
    if r==2:
        break


print(jogadores)
print(F'{"NOME":<10}  {"PARTIDAS":^2}  {"GOLS":^10}  {"TOTAL":>2}')
for i,j in enumerate(jogadores):
    print(f'{i+1}')
    for v in j.values():
        print(f'{v}', end='        ')
    print()

print('-'*30)
print('Levantamento de dados')
print('-'*30)
d = int(input("Deseja consultar os dados de qual jopgador?"))
print(jogadores[d-1])
print(f'DADOS DO {jogadores[d-1]["nome"]}')
for c in range(jogadores[d-1]['partidas']):
    print(f'No jogo {c+1} fez {jogadores[d-1]["gols"][c]} gols.')
# formatação cagadissima

