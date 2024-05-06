print("=-"*15)
print("    <PRINCÍPIO MATEMÁTICO>")
print("=-"*15)
print()
print("-"*28)
print(" Digite o valor de 3 retas")
print("-"*28)
print()
print("Te direi se é possível formar um triangulo com elas...")
r1=float(input("1º reta:"))
r2=float(input("2º reta: "))
r3=float(input("3º reta: "))
print()
if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print()
    print("È possível formar um triangulo!")
    tipo=1
else:
    print()
    print("Não é possível formar um triangulo!")
    tipo=2
print()
print("-"*25)
print("TIPO DO TRIÂNGULO")
print("-"*25)

if tipo==1:
    if r1==r2 and r2==r3 and r3==r1:
        print("Triangulo Equilátero")
    elif (r1==r2 and r2!=r3) or (r3==r2 and r2!=r1) or (r3==r1 and r1!=r2):
        print("Triangulo Isóceles")
    elif r1!=r2!=r3 !=r1:
        print("Triangulo Escaleno")
else:
    print("Não há tipos de triangulo para informar")

    #CONCLUÍDO COM SUCESSO!
