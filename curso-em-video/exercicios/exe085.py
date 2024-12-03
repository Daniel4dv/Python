valores = [[],[]]

for i in range(7):
    valor = (int(input('Digite um valor para adicionar a lista: ')))
    if valor %2 ==0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
 
print(f'Numeros pares: {sorted(valores[0])}')
print(f' Números ímpares: {sorted(valores[1])}')

    
    


