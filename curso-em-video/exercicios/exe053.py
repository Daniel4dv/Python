frase = str(input("Digite uma frase: ")).strip().lower()
print(frase)
palavras = frase.split()
# print(palavras)
junto = ''.join(palavras)
print(junto)
inverso = junto[::-1]
print(inverso)
print()
print("A frase escrita foi {}, o inverso dela é {} portanto...".format(junto,inverso))
if junto == inverso:
    print("\033[32mTemos um palíndromo\033[m")
else:
    print("\033[31mNão temos um palíndromo\033[m")

    #CONCLUÍDO COM SUCESSO!
