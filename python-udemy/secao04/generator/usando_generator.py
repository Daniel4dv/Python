import sys

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# for n in generator:
#     print(n)

# Generator esperando pedir os valores para exibi-los
#como o proprio nome diz, se trata de um gerador de dados
# nao armazena os dados em lugar nenhum
# apenas usa iter para apontar para proximos valores iterando todo o iterable
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))




