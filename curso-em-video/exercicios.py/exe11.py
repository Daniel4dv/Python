a=float(input("Digite a altura de sua parede"))
l=float(input("Digite a largura de sua parede:"))

area=a*l
t=area/2
print()
print("Sua parede tem a area de: {}m²".format(a))
print("A tinta necessária sera {:.2f} litros".format(t))