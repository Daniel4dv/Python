print("=-"*15)
print("    <PRINCÍPIO MATEMÁTICO>")
print("=-"*15)
print()
print("-"*28)
print(" Digite o valor de 3 retas")
print("-"*28)
print()
print("Te direi se é possívewl formar um triangulo com elas...")
r1=float(input("1º reta:"))
r2=float(input("2º reta: "))
r3=float(input("3º reta: "))
print()
if r1+r2>r3 and r2+r3>r1 and r3+r1>r2:
    print()
    print("È possível formar um triangulo!")
else:
    print()
    print("Não é possível formar um triangulo!")

# CONCLUÍDO COM SUCESSO
