def cabecalho():
    print('=-'*25)
    print(F'{"CARTEIRA DIGITAL":^50}')
    print('=-'*25)


def aumentar(x):
    return x+1
def diminuir(x):
    return x-1
def dobro(x):
    return x*2
def metade(x):
    return x/2

def validar(n):
    while True:
        n = input('Digite o valor(%):')
        try:
            n = float(n)
            return n
        except ValueError:
            print('Digite um valor válido!')

def moeda(saldo):
    return f'R${saldo:.2f}.'.replace('.',',')


# porcentagens

def tax(w,por,r):
    por = por/100
    if r==6:
        por +=1
    return w * por



