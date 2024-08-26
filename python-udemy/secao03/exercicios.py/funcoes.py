

def multiplicacao(*args):
    total = 1
    for numero in args:
        total = int(total)*int(numero)
    return total



lista = []
while True:
    print('O que deseja fazer?')
    print('1 - Adicionar mais um numero')
    print('2 - Conferir a multiplicação')
    print('3 - Mostrar lista')
    print('4 - Encerrar programa')
    op = input('>')
    if int(op) ==1:
        numero = (input('adicione um numero:'))
        lista.append(numero) 
    elif int(op) == 2:
        print(multiplicacao(*lista))
    elif int(op)==3:
        print(lista)
    elif int(op) ==4 :
        print("Programa encerrado")
        break


# EXERCICIO 2

def par_impar(x):
    par = False
    if x % 2 ==0:
        par = True
    return par

numero_par = par_impar(5)
print(numero_par)