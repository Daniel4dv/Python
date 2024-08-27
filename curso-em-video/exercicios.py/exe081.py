
numeros = []

while True:
    numero = int(input('Digite um numero para adicionar na lista[0-encerrar]: '))
    if numero != 0:   
        numeros.append(numero)
    else:
        break

print(f'Lista digitada: {numeros}')        
print(f'Foram digitados {len(numeros)} itens')
print(f'Lista de forma decrescente: {sorted(numeros,reverse=True)}')
cinco = False
if 5 in numeros:
    cinco = True
if cinco:
    print(f'Essa lista possui o numero 5 na posição {numeros.index(5)+1}')
else:
    print('Essa lista não possui o numero 5!')