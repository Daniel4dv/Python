from math import sqrt

co=float(input("Digite o valor do cateto oposto: "))
ca=float(input("Digite o valor do cateto adjacente: "))
print()
pco=co**2
pca=ca**2
soma_catetos=pco+pca
print("O valor da hipotenusa é {:.2f}".format(sqrt(soma_catetos)))


#or
#from math import hypot

#co(input("cateto oposto: "))
#ca(input("Cateto adjacente: "))

#hi= hypot(co,ca)

#print("Hipotenusa: ",hi)
