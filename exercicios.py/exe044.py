print("=-=-=-= LOJAS BRASILEIRAS =-=-=-=-")
preço = float(input("Digite o valor da compra: R$"))
print()
print("Qual será a forma de pagamento?")
print("1 - À vista")
print("2 - Cartão de débito")
print("3 - Cartão de crédito")
pay = int(input(">"))

print()
if pay == 1:
    pn = preço-(preço*0.10)
    print("Com o desconto de \033[32m10%\033[m")
    print("O valor da compra fica em \033[32mR${:.2f}\033[m".format(pn))
elif pay == 2:
    pn = preço-(preço*0.05)
    print("Com o desconto de \033[32m5%\033[m")
    print("O valor da compra fica em \033[32mR${:.2f}\033[m".format(pn))
elif pay == 3:
    print("Em quantas vezes deseja parcelar?")
    print("-1 vez")
    print("-2 vezes")
    print("-3 vezes")
    print("-4 vezes")
    print("-5 vezes")
    parcelas = int(input(">"))
    if parcelas <= 2:
        pn = preço
        print("Sem descontos")
        print("O valor da compra fica em R$\033[31m{:.2f}\033[m".format(pn))
    elif parcelas > 2:
        pn = preço*1.20
        print("Com juros de \033[33m20%\033[m")
    print("O valor da compra fica em R$\033[31m{:.2f}\033[m".format(pn))

    print()
    print("{} parcelas com o valor de R$\033[33m{:.2f}\033[m".format(
        parcelas, pn/parcelas))
else:
    print("Opção inválida.Tente novamente")

    # CONCLUÍDO COM SUCESSO!
