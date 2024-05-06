valor = float(input("Digite o valor da casa: R$"))
sal = float(input("Digite o seu salário: "))
anos = float(input("Digite em quantos anos deseja pagar: "))
prestação = valor/(anos*12)
if prestação > (sal*0.30):
    print("-"*25)
    print("O empréstimo foi \033[31m{}\033[m!".format("NEGADO"))
    print("-"*25)
    print()
    print("A prestação ficaria em {:.2f} e como seu salário é {:.2f} excederia o limite de 30% na parcela".format(prestação, sal))
else:
    print("-"*25)
    print("Empréstimo \033[32mAPROVADO\033[m!")
    print("-"*25)
    print()
    print("Valor da parcela: R${:.2f}".format(prestação))

    #CONCLUÍDO COM SUCESSO!