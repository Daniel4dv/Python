lista = []
for l in range(5):
    lista.append(int(input(f'Digite o {l+1}º valor: ')))
print(lista)

print(f'O maior valor foi {max(lista)} e se enconta nas posições ', end='')
for i,v in enumerate(lista):
    if v == max(lista):
        print(f'{i+1}...', end='')
print()

print(f'O menor valor foi {min(lista)} e se enconta nas posições ',end='')

for i,v in enumerate(lista):
    if v == min(lista):
        print(f'{i+1}...', end='')