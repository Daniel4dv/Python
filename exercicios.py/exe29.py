vel=float(input("Velocidade registrada:"))
print()
if vel>80:
    print("VOCÊ FOI MULTADO!")
    vl=(vel-80)*7
    print("Valor a pagar: R$ {:.2f}".format(vl))
else:
    print("Muito bem! Essa velocidade é permitida...")

# CONCLUÍDO COM SUCESSO!