import random
import time
print('Gerando tupla...')
time.sleep(1)
tupla = (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))

print('Tupla gerada: ',tupla)
print('Conclusões')

menor = 50
for i in tupla:
    if i< menor:
        menor = i
print('Menor número: ',min(tupla))    #min = menor numero da tupla
print('Menor numero: ',menor)

print('Maior numero:',max(tupla)) #max = maior numero da tupla

