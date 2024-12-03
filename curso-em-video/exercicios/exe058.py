import random
from time import sleep
pc = random.randint(1, 10)
t = 1
#print(pc)
print("="*60)
print("                 ADVINHE O NÚMERO")
print("="*60)
print("ESTOU PENSANDO EM UM DESSES NÚMEROS")
print("")
for c in range(1, 11):
    print(c, end=" ")
print("\n")
u = int(input("TENTE ADIVINHAR QUAL É: "))
print("\033[38mPROCESSANDO...\033[m")
print("")
sleep(1)
if u == pc:
    print("\033[32mVocê acertou! Parabéns\033[m")
    print("Eu estava pensando no {}".format(pc))
    print("")
    print("Você precisou de só \033[33m{}\033[m tentativa".format(t))

while u != pc:
    t += 1
    if u>pc:
        print("Menos...")
    elif u<pc:
        print("Mais...")
    print("\033[31mVocê errou!\033[m")
    print("Tente novamente")
    u = int(input("Digite um numero entre 1 e 10:"))
    print("\033[38mPROCESSANDO...\033[m")
    print("")
    sleep(1)
    if u == pc:
        sleep(1)
        print("\033[32mVocê acertou! Parabéns\033[m")
        print("Eu estava pensando no {}".format(pc))
        print("")
        print("Você precisou de \033[33m{}\033[m tentativas".format(t))

#CONCLUÍDO COM SUCESSO
