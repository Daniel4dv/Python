numeros = []
while True:
    numero = int(input('Digite um numero para adicionar na lista[0-encerrar]: '))
    if numero != 0:   
        numeros.append(numero)
    else:
        break

print(f'Lista cadastrada:{numeros}')
pares = []
impares = []
for n in numeros:
    if n%2 == 0:
        pares.append(n)
    else:
        impares.append(n)


print(f'Numeros pares da lista:{pares}')
print(f'Numeros impares da lista:{impares}')
