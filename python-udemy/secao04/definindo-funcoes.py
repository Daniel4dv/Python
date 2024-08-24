#definindo funcoes



def saudacao(nome='Sem nome'): #funcao definida com valor de parametro padrao = 'sem nome'
    print(f'Olá {nome}!')       # comandos que a funcao vai executar

def soma(x,y,z):  #parametro
    print(f'{x=} y={y}, {z=}' )
    print(f'x + y + z =', x+y+z)

saudacao('Daniel') # argumento
soma(1,2,4)  #passagem de parametros posicional, no qual x=1 e y=2
soma(y=3,x=2,z=2)  #passagem por valor e nao por posição 

print(1,2,3, sep='-')