import random
import time
import operator

jogo = {
    'jogador1': random.randint(1,6),
    'jogador2': random.randint(1,6),
    'jogador3': random.randint(1,6),
    'jogador4': random.randint(1,6)}

for k,v in jogo.items():
    print(f'O {k} tirou... ',end=' ')
    time.sleep(1)
    print(f'{v}')
 
# colocando dicionario em ordem

raking = {}
raking = sorted(jogo.items(),key=operator.itemgetter(1),reverse=True) #particularidades de um dicionario

print('=-'*30)
print('Raking dos vencedores')
print('=-'*30)

for i, v in enumerate(raking):
    print(f'{i+1}º {v[0]}({v[1]})')
