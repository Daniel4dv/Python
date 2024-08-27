c=1
cont=0
soma=int(0)
maior=0
menor=0
while c==1:
    nmr=int(input("Digite um valor:"))
    if cont==0:
        menor=nmr
    if nmr>maior:
        maior=nmr
    if nmr<menor:
        menor=nmr
    print("DESEJA CONTINUAR")
    print("1 - Sim")
    print("2 - Não")
    c=int(input(">"))
    cont+=1
    soma+=nmr

print("Você digitou {} números".format(cont))
print("Media:{:.2f}".format(soma/cont))
print("Maior: ",maior)
print("Menor:",menor)

#CONCLUÍDO COM SUCESSO