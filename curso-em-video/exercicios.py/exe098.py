import time

def contador(inicio,fim,passo):

    if fim < inicio:
        passo = -abs(passo)
        fim -=1
    else:
        fim +=1
    for x in range(inicio,fim,passo):
        print(x,end='-> ',flush=True)
        time.sleep(.1)

    print('FIM')

def validar(dado):
    while True:
        v = input(f'{dado}: ')
        try:
            v = int(v)
            break
        except ValueError:
            print('Valor inválido. Tente novamente')
    return v

print('Contagem de 1 até 10 (1 em 1):')
contador(1,10,1)
print()
print('Contagem de 10 até 0 (2 em 2):')
contador(10,0,-2)
print()
print('Sua contagem: passe os parametros:')

inicio = validar('Inicio: ')
fim = validar('Fim: ')
passo=0
while passo == 0:
    passo = validar('Passo: ')
    print('O passo não pode ser 0. Tente novamente!')



print(f'Contagem de {inicio} até {fim} ({abs(passo)} em {abs(passo)}) ')
contador(inicio,fim,passo)
