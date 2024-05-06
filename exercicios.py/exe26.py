frase=str((input("Digite uma frase: "))).lower().strip()
print()
print("A letra A aparece {} vezes".format(frase.count("a")))
print("O A aparece pela primeira vez na {}º posição".format(frase.find("a")+1)) #+1 PARA CONSILIAR COM SENSO COMUM HUMANO
print("O A aparece pela última vez na {}º posição".format(frase.rfind("a")+1)) #+1 PARA CONSILIAR COM SENSO COMUM HUMANO

# Concluído com sucesso

