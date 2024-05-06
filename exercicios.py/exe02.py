cores= {'limpar':'\033[m',
        'verde':'\033[32m',
        'azul':'\033[36m',
        'vermelho':'\033[31m',
        'amarelo':'\033[33m'}

n1=int(input("Digite um valor: "))
n2=int(input("Digite outro valor: "))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
p=n1**n2

print()
print("Os resultads dos calculos são:")
print()
print("A soma é {}{}\033[m, a multiplicação é {}{}\033[m, a divisão é {}{:.2f}\033[m.".format(cores['verde'],s,cores['vermelho'],m,cores['azul'],d))
print()
print("A divisão inteira é \033[4;30m{}\033[m, a potencia é \033[4;30m{}\033[m".format(di,p))

# CONCLUÍDO E COLORIDO





