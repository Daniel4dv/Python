# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.



def cria_funcao(funcao):
    def interna(*args,**kwargs):
        for arg in args:
            is_string(arg)
            resultado = funcao(*args,**kwargs)
        return resultado
    return interna   


# sugar syntax
@cria_funcao
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param,str):
        raise TypeError('Parametro deve ser string')
        



# def cria_funcao(funcao,string):
#     def inverte_checado(funcao=funcao):
#         if isinstance(string,str):
#             return funcao
#         else:
#             print('Não é possivel inverter esse item')
#     return inverte_checado()




inverte_string_checada = cria_funcao(inverte_string)

print(inverte_string_checada(123))



# AULA 165


