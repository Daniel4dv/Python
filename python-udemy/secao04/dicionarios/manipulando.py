pessoa = {}

chave = 'nome'
# crud completo
    

pessoa[chave] = None #criando chave e valor para o dicionario
pessoa['sobrenome'] = 'Peixoto'

# del pessoa['sobrenome']

existe = pessoa.get('sobrenome') #metodo para pegar valor de uma chave

if pessoa.get('sobrenome') is None:
    print('Nao existe sobrenome')
else:
    print(pessoa['sobrenome'])

