print("=-"*20)
print("         PROGRESSÃO ARITMÉTICA")
print("=-"*20)

n = int(input("Digite um número:"))
r = int(input("Digite a razão:"))


c = 1
while c <= 10:
    print(n, end=" ")
    n = n+r
    c += 1
print("\n")
x = 1
while x != 0:
    x = int(input("""\nQuantos mais termos voce gostaria de ver?
0 - Encerrar o programa: \n"""))

    print()
    c = 1
    while c <= x:
        print(n, end=" ")
        n = n+r
        c += 1
print()
print("PROGRAMA FINALIZADO")

# CONCLUÍDO COM SUCESSO
