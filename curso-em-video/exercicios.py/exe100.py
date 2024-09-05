import random
lista = []

def sorteia(tam):
    for i in range(tam):
        lista.append(random.randint(1,10))
    return lista

lg = sorteia(5)
print(f'Lista Gerada: {lg}')

soma = 0
for v in lg:
    if v%2==0:
        soma +=v
    

print(f'Somando os valores pares de {lg}: {soma}')


