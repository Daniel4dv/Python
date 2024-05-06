print("=-"*20)
print("        Sequencia de Fibonacci")
print("=-"*20)
c = int(input("Digite quantos termos você quer ver:"))
cont = 0
nmr1 = 1
nmr2 = 0
nmr3 = 1
while cont <= c:
    print(nmr1,end=' -> ')
    nmr2 = nmr1
    nmr1 = nmr3
    nmr3 = nmr3+nmr2

    cont += 1
print("FIM")

# CONCLUÍDO COM SUCESSO
