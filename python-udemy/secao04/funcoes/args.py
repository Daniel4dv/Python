# Argumentos nao nomeados
lista =[ 1,2,3,4]
x,y, *resto = lista

print(resto)

def soma(*args):  # aoi inves de passar variaveis como parametro, usamos o *args para empacotar uma tupla ou lista, no valor retornado ou printado
    total = 0
    for numero in args:
        print(total,'+' ,numero)
        total += numero
        print('Total:',total)

    
    # print(args)

lista = soma(1,2,3,4,5,6)



