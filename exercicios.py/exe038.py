n1=int(input("Digite um número: "))
n2=int(input("Digite outro número: "))
if n1> n2:
    print("\033[32m{}\033[m é maior que \033[31m{}\033[m".format(n1,n2))
elif n2>n1:
    print("\033[32m{}\033[m é maior que \033[31m{}\033[m".format(n2,n1))
else:
    print("Os dois números são \033[33miguais\033[m!")

        #CONCLUÍDO COM SUCESSO!
