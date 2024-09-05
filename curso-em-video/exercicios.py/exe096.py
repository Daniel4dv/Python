def cab(titulo):
    print('=-'*20)
    print(f'{titulo:^40}')
    print('=-'*20)

def area(l,c):
    return l*c


cab('Cálculo de Área')
print('Digite os dados do terreno:')

while True:
    l = input('Largura(m):')
    try:
        l = float(l)
        break
    except ValueError:
        print('Valor inválido. Tente novamente')

while True:
    c = input('Comprimento(m):')
    try:
        c = float(c)
        break
    except:
        print('Valor inválido. Tente novamente')


print(f'Area do terreno:{area(l=l,c=c)}m')
