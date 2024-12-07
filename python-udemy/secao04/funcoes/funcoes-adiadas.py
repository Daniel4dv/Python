def soma (x,y):
    return x+y

def multiplica(x,y):
    return x*y

def cria_funcao(funcao,x):
    def interna(y):
        return funcao(x,y)
    return interna


soma_com_5 = cria_funcao(soma,5)
multiplicaPor10 = cria_funcao(multiplica,10)

print(soma_com_5(10))
print(multiplicaPor10(10))