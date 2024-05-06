print("=-"*15)
print("           TABUADA")
print("=-"*15)
while True:
    n=(int(input("Digite um número para ver a sua tabuada:")))
    if n<0:
        break
    print("=-"*10)
    for c in range (1,11):
        print(f"{n} x {c} = {n*c}")
    print("=-"*10)
    print()
print("\033[31mPROGRAMA ENCERRADO!\033[m")

# CONCLUÍDO COM SUCESSO!


