tot = 0
print("="*60)
print("                      NÚMERO PRIMO")
print("="*60)
n = int(input("Digite um número e direi se ele é primo:"))
print()
for c in range(1, n+1):
    if n % c == 0:
        print("\033[32m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print(c, end=" ")
print("\033[m\n")
print("="*60)
print("\nO número \033[33m{}\033[m foi divisível \033[32m{}\033[m vezes".format(n, tot))
if tot>2:
    print("\033[31mO número não é primo!\033[m")
else:
    print("\033[32mO número é primo!\033[m")

    #CONCLUÍDO COM SUCESSO!
