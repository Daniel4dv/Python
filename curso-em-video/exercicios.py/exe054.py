qm=0
qmn=0
for c in range(1,8):
    ano=int(input("Ano de nascimento: "))
    idade=2023-ano
    if idade>=18:
        qm+=1
    else:
        qmn+=1
print("{} são maior de idade".format(qm))
print("{} são menor de idade".format(qmn))

#CONCLUÍDO COM SUCESSO!
