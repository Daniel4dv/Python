# pessoa = {
#     'nome': 'Daniel',
#     'sobrenome': 'Felipe'
# }

# def insere(**kwargs):
#     return kwargs

# (a1 ,a2),(b1,b2) = pessoa.items()



# pessoa['idade'] = None
# for chave,valor in pessoa.items():
#     print(chave,valor)
    
# outro = {'pessoas': pessoa}

# pessoa2 = {**pessoa,'endereco':'rua A n 50'} # Adicionando um dict como conteudo de dict empacotando ele
# print(pessoa2)

def mostra_argumentos(**kwargs):
    for chave,valor in kwargs.items():
        print(chave,valor)


dicionario = {
    'chave1':'valor1',
    'chave2':'valor2',
    'chave3':'valor3',
    'chave4':'valor4'
}
mostra_argumentos(**dicionario)