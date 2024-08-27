numeros = (int(input("Digite um numero: ")),
        int(input("Digite mais um numero: ")),
        int(input("Digite mais um numero: ")),
        int(input("Digite mais um numero: ")))

print('Tupla digitada:',numeros)

print(f'O 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O 3 apareceu pela primeira vez na posição {numeros.index(3)+1}')
else:
    print("O numero 3 não apareceu!")

print('Os valores pares da tupla são: ', end='')
for n in numeros:
    if n %2==0:
        print(n,end=' ')


# gg easy peasy

