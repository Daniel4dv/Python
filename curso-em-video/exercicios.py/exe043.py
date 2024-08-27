peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura:"))
imc=float(peso/altura**2)
print()
if imc<18.5:
    print("IMC:{:.2f} ".format(imc))
    print("Seu IMC diz que está abaixo do peso")
elif imc<25:
    print("IMC:{:.2f} ".format(imc))
    print("Seu IMC diz que está no peso ideal")
elif imc>=25 and imc<30:
    print("IMC:{:.2f} ".format(imc))
    print("Seu IMC diz que está em sobrepeso!")
elif imc>=30 and imc<=40:
    print("IMC:{:.2f} ".format(imc))
    print("Seu imc diz que está em estado de obesidade!")
else:
    print("IMC:{:.2f} ".format(imc))
    print("Seu IMC diz que está GORDO PRA CACETEKKKKKKKKKKKKKKKK")

    #CONCLUÍDO COM SUCESSO!
