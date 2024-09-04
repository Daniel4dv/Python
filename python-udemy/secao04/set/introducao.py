lista = [1,1,1,2,2,2,2,3,3,4,4,4,5,5,6,6,7,7,8,8,8,8,8,9,9,9,9,9,9,9,9,9]
lista = set(lista)
lista = list(lista)

# nome = set(1,2,(123,))  #nao sei pq nao funcionou

# Ao converter a lista em set voce remove todos os valores trepetidos

print(lista,type(lista))

# PODE FAZER TAMBEM
print('contem/ nao contem')
print(5 in lista) # retorna True or None pra ocorrencia de ter item na respectivo set


exit()

# E TIPO UM DICIONARIO MAS NAO TEM CHAVES, APENAS VALORES
meu_set = set() # SET VAZIO
meu_set = {1,1,1,1,2,2,1,5.5} # O set ja elimina valores repetidos por padrão ao printar (os valores repetisos nãos erao exibidos)
print(meu_set)