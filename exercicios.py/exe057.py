s='m'
print("="*50)
print("               CADASTRO DE CLIENTE")
print("="*50)
print("Digite seu sexo:")
print("M - Masculino")
print("F - Feminino")
s=str(input(">")).strip()
print("")
while s not in ("mfMF"):  
    print("\033[31mSexo inválido\033[m")
    print("Digite novamente seu sexo:")
    s=str(input("Digite seu sexo:"))
    print("")
print("\033[32mCADASTRO CONCLUÍDO\033[m")

#CONCLUÍDO COM SUCESSO
