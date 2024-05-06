from time import sleep
print("Digite 2 números:")
n1=int(input(">"))
n2=int(input(">"))

c=0
while c != 5:
    print("Carregando...")
    print()
    sleep(2)
    print("O QUE DESEJA FAZER?")
    print("[1] SOMAR")
    print("[2] MULTIPLICAR")
    print("[3] SABER QUAL É O MAIOR")
    print("[4] TROCAR OS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")
    c=int(input(">"))
    if c==1:
        r=n1+n2
        print("Soma dos números: {}".format(r))
        print("="*20)
    elif c==2:
        r=n1*n2
        print("Multiplicação dos números: {}".format(r))
        print("="*20)
    elif c==3:
        if n1>n2:
            r=n1
            print("Número maior:{}".format(r))
            print("="*20)
        elif n2>n1:
            r=n2
            print("Número maior:{}".format(r))
            print("="*20)
        else:
            print("Os dois números são iguais")
            print("="*20)
    elif c==4:
        print("Digite 2 números:")
        n1=int(input(">"))
        n2=int(input(">"))

print("PROGRAMA ENCERRADO!")

#CONCLUÍDO COM SUCESSO!!!