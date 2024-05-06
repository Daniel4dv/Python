mai=float(0)
men=float(0)
for c in range(1,6):
    p=float(input("Digite o peso da {}º pessoa: ".format(c)))
    if c==1:
        mai=p
        men=p
    if p>mai:
        mai=p
    if p<men:
        men=p
print("Maior peso:{}kg".format(mai))
print("Menor peso: {}kg".format(men))

#CONCLUÍDO COM SUCESSO!