import random
lista = []

def sorteia(tam):
    for i in range(tam):
        lista.append(random.randint(1,10))
    return lista

lg = sorteia(5)
print(f'Lista Gerada: {lg}')
print()



def somapar(lista):
    soma = 0
    for v in lista:
        if v%2==0:
            soma +=v
    return soma

soma = somapar(lg)

print(f'Somando os valores pares de {lg}: {soma}')


