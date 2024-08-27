soma=0
cont = 0
for c in range(1,501):
    if c%2 !=0 and c%3 == 0:
        soma=soma+c
        cont+=1
print("Somatório dos números impares divisíveis por 3:",soma)
print("Foram somados {} números".format(cont))

#CONCLUÍDO COM SUCESSO!


