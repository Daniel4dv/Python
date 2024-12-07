# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def inverte_string(string):
    return string[::-1]



def cria_funcao(funcao):
    def interna(string):
        return funcao,string
    return interna    



# def cria_funcao(funcao,string):
#     def inverte_checado(funcao=funcao):
#         if isinstance(string,str):
#             return funcao
#         else:
#             print('Não é possivel inverter esse item')
#     return inverte_checado()



inverte_string_checada = cria_funcao(inverte_string)

print(inverte_string_checada('bolado'))



# AULA 165


