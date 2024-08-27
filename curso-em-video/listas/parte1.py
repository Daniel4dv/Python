import random
import sys


lista = ['segunda','terça','quarta','quinta','sexta']

aleatorios = list(range(random.randint(0,10),random.randint(20,50),random.randint(1,5)))


print(aleatorios)
print(f'Essa lista contem {len(aleatorios)} itens')



print(lista)

lista.append('sábado') #adiciona mais um elemento na ultima casa
print(lista)
lista.insert(0,'domingo')  # adiciona um elemento no indice desejado
print(lista)

# del lista[0]
lista.pop()  #remove o ultimo item da lista caso nao adicione indice
# lista.remove('segunda')
print(lista)

# copia e ligaçao entre listas
a=[1,2,3,4]
b= a[:]
b.remove(3) #ira remover o item das duas listas a nao ser que voce use [:] que faz uma copia dos itens ao inves de ligar as listas
print(a)
print(b)
exit()
