lista = []
for l in range(5):
    lista.append(int(input(f'Digite o {l+1}º valor: ')))
print(lista)

print(f'O maior valor foi {max(lista)} e se enconta na posição {lista.index(max(lista))+1}')

print(f'O menor valor foi {min(lista)} e se enconta na posição {lista.index(min(lista))+1}')
