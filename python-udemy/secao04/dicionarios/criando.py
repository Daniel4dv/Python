 # dicionario é criado com chaves mas é preciso indicar os indices: nome,idade,peso, etc

pet = dict(nome = 'Luna',genero='Femea') # outro jeito de criar

pessoa = {
    'nome': 'Luis otavio', #definindo indices (com strings) e valores
    'Sobrenome': 'Peixoto',
    'idade' : 18,
    'enderecos' : [
        {'rua': 'tal','numero': 56 } ,
        {'rua': 'y','numero': 120 },
    ],
}

# print(pessoa['nome'])

print('Dados cadastrais:' )
for chave in pessoa:
    print(f'{chave}: ',end='')
    print(pessoa[chave])
