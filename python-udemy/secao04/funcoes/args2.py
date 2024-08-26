
def soma(*args): 
    total = 0
    for numero in args: # fazendo a iteração dos itens presentes em args(tupla)
        total += numero
    return total


lista = (1,34,52,34534,346,4567,342,5423,432,7,457,45,2344)
print (soma(*lista))  #*tupla desempacota os valores da tupla ou lista para usar na funcao