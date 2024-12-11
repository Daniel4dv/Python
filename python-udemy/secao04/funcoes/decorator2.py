def decoradora(func):
    print('decoradora 1')

    def aninhada(*args,**kwargs):
        print('Aninhada')
        resultado = func(*args,**kwargs)
        return resultado
    return aninhada



@decoradora
def soma(x,y):
    return x+y