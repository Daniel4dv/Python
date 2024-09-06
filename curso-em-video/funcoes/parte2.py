# CRIANDO DOCSTRINGS DE FUNCOES PARA EXPORTZACAO

def ola():
    '''
    exibe uma mensagem de ola mundo
    '''
    print('Ola mundo')

# COMANDO HELP DE CONSULTA DE DOC PARA ENTENDER O COMANDO/FUNCAO
help(ola)

print('=-'*20)
print('PARAMETROS OPCIONAIS')
print('=-'*20)
# parametros opcionais

def soma(*num): # VALOR PADRAO PARA PARAMETRO EM CASO DE NAO INFORMAÇAO DO MESMO
    print(sum(num))

# soma(1,4,6)
soma()

print('=-'*20)
print('ESCOPO DE VARIAVEIS ')
print('=-'*20)

def fatorial(n):
    for i in range((n-1),0,-1):
        n *=i
    return n


print(f'Fatorial:',fatorial(5))