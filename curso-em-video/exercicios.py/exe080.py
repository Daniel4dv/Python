numeros = []

for n in range(5):
    numero = int(input('Digite um numero para adicionar na lista: '))
    if numeros == []:
        numeros.append(numero)
    for i in numeros:
        if numero >numeros[i]:    
            numeros.insert[i+1]

print(numeros)

     