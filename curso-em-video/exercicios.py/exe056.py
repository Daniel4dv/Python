m20 = 0
somaidades = 0
maiorid = 0
hqtd = 0
for c in range(1, 5):
    print("=======-- {}º Pessoa --======".format(c))
    n = str(input("Nome: ".format(c)))
    idade = int(input("Idade: ".format(c)))
    print("Sexo:".format(c))
    print("1 - Masculino")
    print("2 - Feminino")
    sexo = int(input(">"))
    somaidades += idade
    if sexo == 1:
        hqtd += 1
        if idade > maiorid:
            maiorid = idade
            hold = n
    if sexo == 2:
        if idade < 20:
            m20 += 1
    if hqtd == 0:
        hold = 0

media = somaidades/4

print()
print("Média de idades:{}".format(media))
print("Homem mais velho:{}".format(hold))
print("Quantidade de mulheres com menos de 20 anos: {}".format(m20))

# CONCLUÍDO COM SUCESSO!
