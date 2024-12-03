ano = int(input("Digite o ano que você nasceu: "))
idade = 2023-ano
if idade < 18:
    print("Sua hora ainda não chegou!")
    anoc=2023+(18-idade)
    print("Faltam {} anos pra você poder se alistar".format((18-idade)))
    print("Em ",anoc)
elif idade == 18:
    print("Sua hora chegou")
    print("Corra para se alistar")
else:
    print("Você ja devia ter se alistado")
    anoc=2023-(idade-18)
    print("{} anos atrás".format((idade-18)))
    print("Em ",anoc)

    # CONCLUÍDO COM SUCESSO!
