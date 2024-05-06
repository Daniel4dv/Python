from random import randint
from time import sleep

print("=-"*10)
print("    JO-KEM-PÔ")
print("=-"*10)
print()
print("Pedra papel ou tesoura?")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")
jogador=int(input(">"))
print()

pc=randint(1,3)
# print(pc)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(0.5)
print()
print("-Computador") 
if pc==1:
    print("Eu escolho Pedra")
elif pc==2:
    print("Eu escolho Papel")
else:
    print("Eu escolho tesoura")

print()


if pc==1 and jogador==1:
    print("EMPATE")
    print("Vamos denovo!")
elif pc==2 and jogador==2:
    print("EMPATE")
    print("Vamos denovo!")
elif pc==3 and jogador==3:
    print("EMPATE")
    print("Vamos denovo!")

if pc==1 and jogador==3:
    print("EU ganhei HAHAHA")
    print("Pedra quebra tesoura")
elif pc==3 and jogador==2:
    print("EU ganhei HAHAHA")
    print("Tesoura corta papel")
elif pc==2 and jogador==1:
    print("Eu ganhei HAHAHA")
    print("Papel embrulha pedra")

if pc==1 and jogador==2:
    print("Droga, eu perdi...")
    print("Papel embrulha pedra")
elif pc==2 and jogador==3:
    print("Droga! Eu perdi")
    print("Tesoura corta papel!")
elif pc==3 and jogador==1:
    print("Droga! Eu perdi...")
    print("Pedra quebra tesoura ")

    #CONCLUÍDO COM SUCESSO!
