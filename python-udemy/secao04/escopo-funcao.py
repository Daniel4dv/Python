
# def escopo():
        # x esta sendo definido dentro do escopo da funcao / variavel local
    # print(x)

# print() #aqui, x nao tem valor, nao foi definido

# x = 4  # variavel global
# escopo()
b= 5
a =4
def funcao1(): #criando uma funcao
    global a
    a=1  #variavel da funcao // nao altera variaveis globais, como o a criado anteriormente, continuara valendo 5 apos executar a funcao
    def funcao2(): #definindo uma funcao dentro de outra funcao
        a = 2
        print(f'funcao2 = {a}')      
    funcao2()   #execuntando a funcao criada dentro da primeira funcao
    print(f'funcao 1  = {a}')

funcao1()
print(a)






