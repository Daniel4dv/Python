print("Digite 3 números inteiros...")
n1 = int(input("Primeiro:"))
n2 = int(input("Segundo:"))
n3 = int(input("Terceiro:"))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

print("{} foi o maior número digitado!".format(maior))

if n1 < n1 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print("{} foi o menor número digitado!".format(menor))

# CONCLÍDO COM SUCESSO!
