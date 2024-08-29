import random
import time
j = 0
jogo = []


print('=-'*25)
print(f'{"TELA SENA DO MILHÃO":^50}')
print('=-'*25)
jogos = []
qtd = int(input('Quantos jogos deseja gerar? '))
for i in range(qtd):
    while j<6:
        numero = random.randint(1,60)
        if numero in jogo:
            continue
        else:
            jogo.append(numero)
        j+=1
    j = 0
    jogos.append(jogo[:])
    jogo.clear()
    
i=0
print('=-'*25)
print(f'{"JOGOS GERADOS":^50}')
print('=-'*25)
for i in range(qtd):
    print(f'Jogo {i+1}: {sorted(jogos[i])}')
    time.sleep(1)

    