# def soma(x,y):
#     return x+y  # ao inves de printar, retornamos, para poder retornar um valor para uma variavel podendo utilizar posteriormente,
#                 # o return tambem encerra a funcao, ou seja, tudo que seguir o return sera encerrado e nao executado

# soma1 = soma(2,2)  # soma1 esta recebendo o valor que a funcao soma retorna
# soma2 = soma(3,3)
# print (soma1 + soma2)

def funcao_condicional(a,b):
    if a > b:
        return a-b
    return a+b


print(funcao_condicional(8,5))