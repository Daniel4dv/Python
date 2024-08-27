c=0
mais18=0
homens=0
m20=0
sexo=0
esc=0
print("=-"*15)
print("          CADASTRO")
print("=-"*15)
while True:
    c+=1
    id=int(input(f"Digite a idade da {c}º pessoa:"))
    print()
    while sexo!=1 and sexo!=2:
        print(f"Sexo da {c}º pessoa:")
        sexo=int(input("[1] Masculino [2] Feminino:"))
        if sexo!=1 and sexo!=2:
            print()
            print("\033[33mOpção inválida! Tente novamente\033[m")
    if sexo==2:
        if id<20:
            m20+=1
    if sexo==1:
        homens+=1
    if id>18:
        mais18+=1
    while esc!=1 and esc !=2:
        print()
        print("=-"*15)
        print("Deseja continuar cadastrando?")
        print("1 - \033[32mSim\033[m")
        print("2 - \033[31mNão\033[m")
        esc=int(input(">"))
        print("=-"*15)
        if esc!=1 and esc !=2:
            print()
            print("\033[33mOpção inválida! Tente novamente\033[m")
    if esc==2:
        break
    sexo=0
    esc=0
print()
print("\033[mCADASATRO CONCLUÍDO\033[m")
print()
print(f"Pessoas com mais de 18 anos:{mais18}")
print(f"Quantidade de homens cadastrados:{homens}")
print(f"Mulheres com menos de 20 anos:{m20}")

# CONCLUÍDO COM SUCESSO

    