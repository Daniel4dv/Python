def maior(lista):
    print(max(lista))

def maior_arg(*arg):
    maior = 0
    for i in arg:
        print(f'{i}',end=' ')
        if i == arg[0]:
            maior = i
        else:
            if i> maior:
                maior = i
    print(f'Maior: {maior}')
    # arg = list(arg)
    # return max(arg)

v = 1
lista = []
while v!=0:
    while True:
        v = input('Digite um valor para adicionar na lista: ') 
        try:
            v = int(v)
            if v==0:
                break
            lista.append(v)
            print(lista)
        except ValueError:
            print('Valor invalido! Tente novamente')

print()
print(lista)
print(f'Maior valor da lista:',end=' ')
{maior(lista)}

print('=-'*20)

maior_arg(8,4,5,6,9,3,1)
