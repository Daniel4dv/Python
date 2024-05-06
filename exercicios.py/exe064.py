nmr=0
c=0
soma=0
print("=-"*20)
print("SOMA E CONTADOR DE NÚMEROS")
print("=-"*20)

while nmr!=999:
    nmr=int(input("Digite um valor [999 para encerrar]:"))
    if nmr!=999:
        soma+=nmr
        c+=1
print("Soma: {}".format(soma))
print("Foram digitados: {}".format(c))

# CONCLUÍDO COM SUCESSO