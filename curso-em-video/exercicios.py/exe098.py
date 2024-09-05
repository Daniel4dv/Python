import time

def contador(inicio,fim,passo):
    for x in range(inicio,fim,passo):
        print(x,end='-> ',flush=True)
        time.sleep(.1)
    print('FIM')

print('Contagem de 1 até 10 (1 em 1):')
contador(1,10,1)
print()
print('Contagem de 10 até 0 (2 em 2):')
contador(10,-1,-2)
print()
print('Sua contagem: passe os parametros:')
while True:
    inicio = input('Inicio: ')
    try:
        inicio = int(inicio)
        break
    except ValueError:
        print('Valor invalido.Tente novamente!')
while True:
    fim = input('Fim: ')
    try:
        fim = int(fim)
        break
    except ValueError:
        print('Valor invalido.Tente novamente!')
while True:
    passo = input('Passo: ')
    try:
        passo = int(passo)
        if passo ==0:
            print('O passo não pode ser 0')
        else:
            break
    except ValueError:
        print('Valor invalido.Tente novamente!')

print(f'Contagem de {inicio} até {fim} ({abs(passo)} em {abs(passo)}) ')
contador(inicio,fim,passo)
