print("Digite as notas do aluno: ")
n1=float(input(">"))
n2=float(input(">"))
media=(n1+n2)/2
if media<5:
    print("-"*15)
    print("\033[31mREPROVADO\033[m")
    print("-"*15)
    print("Média: ",media)
    print("Estude mais na próxima!!!")
elif 5<= media <7:
    print("-"*15)
    print("\033[33mRECUPERAÇÃO\033[m")
    print("-"*15)
    print("Média: ",media)
    print("Boa sorte na recuperação")
else:
    print("-"*15)
    print("\033[32mAPROVADO\033[m")
    print("-"*15)
    print("Média: ",media)
    print("Parabéns pela aprovação!")

    #CONCLUÍDO COM SUCESSO!
