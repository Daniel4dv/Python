numeros = []

while True:
    numero = int(input(('Digite um numero para ser adicionado/digite 0 para parar de adicionar: ')) )

    if numero != 0:
        if numero in numeros:
            print('Esse numero ja esta na lista')
            continue
        else:
            numeros.append(numero)
    else:
        print('programa encerrado!')
        break

numeros.sort()
print(f'Lista digitada: {numeros}')

     
    