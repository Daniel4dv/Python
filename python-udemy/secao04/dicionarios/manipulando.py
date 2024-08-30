pessoa = {}

# chave = 'nome'
# crud completo
    

# pessoa[chave] = None #criando chave e valor para o dicionario
pessoa['sobrenome'] = 'Peixoto'

del pessoa['sobrenome']  #apaga a chave sobrenome e o valor que haja nela

existe = pessoa.get('sobrenome') #metodo para pegar valor de uma chave, por padrão, retorna None(null) caso a chave nao exista


chave = ['nome','sobrenome','idade','sexo']

for c in chave:
    pessoa[c] = None  # dicionario criado com um for atraves de uma lista de keys

print(pessoa.get('sobrenome'))

exit()
if pessoa.get('sobrenome') is None:
    print('Nao existe sobrenome')
else:
    print(pessoa['sobrenome'])






