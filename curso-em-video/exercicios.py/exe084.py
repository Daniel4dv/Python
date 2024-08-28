pessoas = []
qtd_pessoas = 0
maior_peso = 0

while True:

    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    pessoas.append(nome)
    qtd_pessoas +=1
    pessoas.append(peso)
    if maior_peso == 0:
        maior_peso = peso
    else:
        if peso> maior_peso:
            maior_peso = peso


    r = input('Quer continuar adicionando? [S/N]')
    if r in 'Nn':
        break

print(pessoas)
print(pessoa)