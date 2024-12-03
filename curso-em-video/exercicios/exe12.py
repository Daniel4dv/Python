p=float(input("Digite o preço do produto: R$"))

d=p*0.05
print()
print("Preço com desconto aplicado: R${:.2f}".format(p-d))

p2=float(input("Digite o preço do outro produto: R$"))

d2=p2*5/100
print()
print("Preço com desconto aplicado: R${:.2f}".format(p2-d2))