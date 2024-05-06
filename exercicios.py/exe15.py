d=int(input("Quantos dias o carro foi alugado?"))
km=float(input("Quantos KM foram percorridos?"))
pd=d*60
pkm=km*0.15
print()
print("O valor do aluguel pelos dias ficou em R${:.2f}\nO valor do aluguel pela quilometragem ficou em R${:.2f}".format(pd,pkm))
print()
print("Preço total do aluguel: R${:.2f}".format(pd+pkm))