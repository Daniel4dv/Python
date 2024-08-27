nome = str(input("digite o seu nome completo: ")).strip()
print()
print("CAPS LOCK: {}".format(nome.upper()))
print("Tudo minúsculo: {}".format(nome.lower()))
dividido = nome.split()
print("Seu nome tem {} letras".format(len(nome)-nome.count(" ")))  


print("Seu primeiro nome tem {} letras".format(len(dividido[0])))

# concluído com sucesso
