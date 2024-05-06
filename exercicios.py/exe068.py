import random
vit=0
der=0
print("=-"*20)
print("         JOGO DO ÍMPAR OU PAR")
print("=-"*20)
esc=0
while True:
    while esc not in (1,2):
        print("Escolha entre ímpar ou par")
        print("1 - Ímpar")
        print("2 - Par")
        esc=int(input(">"))
        if esc!= 1 and esc!=2:
            print("\033[33mEscolha inválida! Tente novamente\033[m")
            print()
    ganhou=bool(False)

    jog=int(input("Digite seu número:"))
    pc=random.randint(1,10)
    soma=jog+pc 

    if esc==1 and soma%2!=0:
        ganhou=True
    elif esc==2 and soma%2==0:
        ganhou=True
    print()
    print(f"Você escolheu o número {jog}")
    print(f"Eu Escolhi o número {pc}")
    print(f"A soma dos números é {soma}")
    if soma%2==0:
        print("Então o resultado é PAR")
    else:
        print("Então o resultado é ÍMPAR")
    print()

    if ganhou==True:
        print("\033[32mParabéns! Você ganhou\033[m")
        vit+=1
    elif ganhou==False:
        print("\033[31mVocê Perdeu!\033[m")
        der+=1
    print("Deseja continuar jogando?")   
    print("1 - Sim")
    print("2 - Não")
    esc2=int(input(">"))
    if esc2==2: 
        break

print("PROGRAMA ENCERRADO!")
print()
print(f"\033[32mVitórias\033[m:{vit}")
print(f"\033[31mDerrotas\033[m:{der}")

    


