nmr=int(input("Digite um número: "))
print()
print("Selecione qual conversão deseja fazer: ")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
cvs=int(input(">"))
if cvs==1:
    print("Binario ne safadin")
    print("Número:",nmr)
    print("Binário:",bin(nmr)[2:])
elif cvs==2:
    print("Octal ne safadin")
    print("Número:",nmr)
    print("Octal: ",oct(nmr)[2:])
elif cvs==3:
    print("Hexadecimal ne safadin kkk")
    print("Número: ",nmr)
    print("HExadecimal: ",hex(nmr)[2:])
else:
    print("Opção inválida")

    # CONCLUÍDO COM SUCESSO!