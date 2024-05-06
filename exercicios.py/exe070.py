total=0
m1000=0
mb=0
c=0
print("=-"*20)
print("           LOJA DO RATÃO")
print("=-"*20)
while True:
    c+=1
    nome=str(input(f"Digite o nome do {c}º produto:"))
    p=float(input(f"Digite o preço do {c}º produto:"))
    if c==1:
        mb=p
    if p<=mb:
        mb=p
        nmb=nome
    total+=p
    if p>1000:
        m1000+=1

    esc=0
    while esc!=1 and esc!=2:
        print()
        print("=-"*15)
        print("Deseja continuar o cadastro?")
        print("1 - Sim")
        print("2 - Não")
        esc=int(input(">"))
        print()
        print("=-"*15)
        if esc!=2 and esc!=1:
            print("\033[33mOpção inválida! Tente novamente\033[m")
    if esc==2:
        break
print("\033[32mCADASRTO CONCLUÍDO\033[m")
print("=-"*15)

print(f"Preço total:{total:.2f}")
print(f"Quantidade de produtosa que custam mais de R$1000:{m1000}")
print(f"Produto mais barato da compra:{nmb}")

# CONCLUÍDO COM SUCESSO

