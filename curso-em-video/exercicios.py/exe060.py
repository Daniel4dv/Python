n=int(input("Digite um número:"))
fat=n
c=n
print()
print("Calculando {}!".format(c))
while c>0:
    print("{} ".format(c),end="")
    print("x " if c>1 else "",end="")
    c-=1
    if c>0:
        fat=fat*c
print("\n")    
print("O fatorial de {} é {}".format(n,fat))

#CONCLUÍDO COM SUCESSO 


