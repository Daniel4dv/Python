print("=-"*20)
print("             Calculadora")
print("=-"*20)
soma=int(0)
cont=int(0)
while True:
    n=int(input("Digite um número:"))
    if n==999:
        break
    cont+=1
    soma+=n
print("=-"*15)
print("Programa Encerrado")
print("=-"*15)
print(f"Foram digitados {cont} números")
print(f"A soma dos números digitados é {soma}")

# CONCLUÍDO COM SUCESSO

