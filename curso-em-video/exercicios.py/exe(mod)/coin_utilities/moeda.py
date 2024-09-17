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



def moeda(saldo):
    return f'R${saldo:.2f}'


# porcentagens

def tax(w,por,r):
    w = float(w)
    if r==5:
        por = por/100
        t = w *por
        return w-t
    elif r==6:
        por = 1+ (por/100)
        return w * por

