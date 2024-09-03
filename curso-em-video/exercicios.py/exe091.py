import random

jogada = 0
jogadas = {}

for i in range(4):
    jogada = random.randint(1,6)
    jogadas[f'dado{i+1}'] = jogada

print(jogadas)

for i,d in enumerate(jogadas.values()):
    print(f'Jogador{i+1} : {d}')
        
jogadas = dict(sorted(jogadas.values(),reverse=True))
print('Ranking dos Maiores valores')

print(jogadas)
