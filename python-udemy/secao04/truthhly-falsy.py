lista = []
tupla = ()
palavra = ''
conjunto = set()
dicionario = {}
inteiro = 0
flutuante = 0.0
nada = None
booleano = False
intervalo = range(0)


def truth(valor):
    return 'truthy' if valor else 'Falsy'


print(truth(lista))
print(truth(tupla))
print(truth(palavra))
print(truth(conjunto))
print(truth(dicionario))
print(truth(inteiro))
print(truth(flutuante))
print(truth(nada))
print(truth(booleano))
print(truth(intervalo))