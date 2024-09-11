def nao_aceita_zero(n):
    if n==0:
        raise ZeroDivisionError('Voce esta tentando dividir por 0')
    return True

def proibe_str(fi):
    tipo = type(fi)
    if not isinstance(fi,(int,float)):
        raise TypeError(f'O {fi} deve ser int ou float. \n'
                        f'Voce digitou um dado do tipo "{tipo.__name__}"')

def divide(n,d):

    proibe_str(n)
    proibe_str(d)
    nao_aceita_zero(d)
    return n / d
   
   
print(divide('5',3))