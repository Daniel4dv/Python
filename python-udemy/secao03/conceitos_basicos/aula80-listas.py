lista = list('') #convete algum dado para lista

lista = [] #criando a lista // lista é uma var mutável // suporta varios tipos de dados

# ------- 0 --- 1 ------ 2 ------ 3 --
lista = [123 , True , 'Daniel' , 1.5] # criar

print(lista)
print(lista[1])

lista[2] = 'Maria' #alterar
del lista[0] #deletar

lista.append(50) #adiciona um item ao final da lista
print(lista)
ultimo_valor =  lista.pop() #remove o ultimo elemento da lista
print(lista)
lista.pop(0)  #REMOVE UM ELEMENTO ESPECIFICO DA LISTA
print(ultimo_valor)
print(lista)

lista.clear() # limpa todo o conteudo da lista

lista.insert(3,50) # insere um vaslor especifico em uma posição especifica na lista (indice,valor)