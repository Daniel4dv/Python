jogador = {}

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))
gols = []
for g in range(partidas):
    gol = int(input(f'Quantos gols ele fez na partida {g+1}: '))
    gols.append(gol)

jogador['gols'] = gols
jogador['total'] = f'{sum(gols)} gols em {partidas} partidas'

print(jogador)
print('=-'*25)
for k,v in jogador.items():
    print(f'{k} : {v}')
print('=-'*25)

for g in range(partidas):
    print(f'Na partida {g+1}, {jogador["nome"]} marcou {jogador["gols"][g]} gols.')


