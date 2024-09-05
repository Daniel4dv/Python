lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordem(item):
#     return item['nome']

def exibir(lista):
    for d in lista:
        print(d)

# lista.sort(key=ordem)

# expressao lambda // faz isso de uma forma mais rapida

lista.sort(key = lambda item:item['nome'])
lista_ordenada_nome =  sorted(lista, key = lambda item:item['nome'] )
lista_ordenada_sobrenome =  sorted(lista, key = lambda item:item['sobrenome'] )

exibir(lista_ordenada_nome)
print()
exibir(lista_ordenada_sobrenome)