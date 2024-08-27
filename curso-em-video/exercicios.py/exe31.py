km=float(input("Digite a distancia em KM de sua viagem: "))
if km>200:
    p=km*0.45
    print("Por R$0,45 p/km")
    print("Sua viajem fica em {:.2f}".format(p))
else:
    p=km*0.50
    print("por R$0,50 p/ Km")
    print("Sua viajem fica em {:.2f}".format(p))

    # CONCLUÍDO COM SUCESSO!