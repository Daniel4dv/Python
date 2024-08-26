
def soma(x,y,z=None):
    if z is not None: #usando o is not none ao inves de if z voce faz com que o programa aceite 0 como valor válido e mostrara o z=0 normalmente
        print(f'{x=} {y=} {z=}' ,'soma=',x+y+z)
    else:
        print(f'{x=} {y=}' ,'soma=',x+y)


soma(1,5,0)

# da mesma forma que um argumento com valor deve ser seguido de apenas argumentos com valor, parametros com valor devem ser seguidos 
# por parametros por valor

def multiplicacao(a=4,b=3): # se a tiver valor padrao, b nao pode ficar sem valor padrao
    print(a*b)

multiplicacao()

def multiplicacao(a,b=None):
    if b is not None:
        print(a*b)
    else:
        print(a)

multiplicacao(2)

        
