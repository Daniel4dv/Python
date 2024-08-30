pessoa  = {
    'nome': 'Daniel',
    'sobrenoms': 'Peixoto'
}

print(pessoa.__len__()) # len(pessoa)  -  conta a quantiadade de chaves
print(list(pessoa.keys()))  #metodo que mostra(itera) as chaves do dicionario, (convertida para lista para otimizar uso)
print(list(pessoa.values()))  # Metodo que mostra itera os valores das chaves do dicionario tambem covertidas para lista.
print(list(pessoa.items()))  # Metodo que mostra(itera) os valores e as chaves do dicionario em tuplas, passados para uma lista.
pessoa.setdefault('emprego','desempregado')  #determina um valor padrao pra caso tente exibir uma chave que nao existe ou possua valor nulo
print(pessoa['emprego'])



# for valor in pessoa.values():
#     print(valor)

# for chave,valor in pessoa.items(): # itera os 2 itens de cada tupla em 2 variaveis
#     print(chave,valor)

