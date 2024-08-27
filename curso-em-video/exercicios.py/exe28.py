import random # modulo para calculo de randomização
from time import sleep # módulo para timer
x=random.randint(0,5)
print("-"*26)
print("    Adivinhe o número")
print("-"*26)
print("Estou pensando em um número entre 0 e 5")
y=int(input("Tente adivinhar: "))
print()
print("PROCESSANDO...")
sleep(1) # programa ira esperar 1 segundo para continuar...
if y==x:
    print("Tinha pensado em {}".format(x))
    print("DROGA! Você acertou, esses humanos...")
elif y>5:
    print("Entre 0 e 5 burrãokkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
    print()
    print("Tinha pensado em {}".format(x))
else:
    print("Tinha pensado em {}".format(x))
    print("HAHAHA! Você errou kkkk")

    # CONCLUÍDO COM SUCESSO