# ========================================================
                        # aula 167
# ========================================================

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

dez_cinco = soma(10,5)
print(dez_cinco)