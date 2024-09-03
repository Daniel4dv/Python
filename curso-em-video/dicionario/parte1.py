locadora = []
filme = {}


for f in range(3):
    filme['nome'] = str(input('Digite o nome do filme: '))
    filme['ano'] = int(input('Digite o ano do filme:'))
    filme['diretor'] = str(input('Digite o diretor do filme: '))
    locadora.append(filme.copy())  #fazendo copia/fatiamento no dicionario
    filme.clear()

for li,l in enumerate(locadora):
    print(f'Filme {li+1}:')
    for k,v in l.items():
        print(f'{k}:{v}')
    print('=-'*20)







exit()
dicionario = {
    'nome': 'Pedro','idade':34
}

dicionario['sexo']='M' #criando elemento
del dicionario['idade'] #deletando dicionario
dicionario['peso'] = 65.9

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

for k,v in dicionario.items():
    print(f'>{k} : {v}')

