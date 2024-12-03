pessoa = []
pessoas = []
maior_peso = 0
menor_peso = 0
mais_pesados =[]
mais_leves =[]

while True:

    pessoa.append(input('Digite o nome: '))
   
    pessoa.append(float(input('Digite o peso: ')))
    pessoas.append(pessoa[:])
    if maior_peso == 0:
        maior_peso = pessoa[1]
    else:
        if pessoa[1]> maior_peso:
            maior_peso = pessoa[1]

    if menor_peso == 0:
        menor_peso = pessoa[1]
    else:
        if pessoa[1]< menor_peso:
            menor_peso = pessoa[1]
    pessoa.clear()

    r = input('Quer continuar adicionando? [S/N]')
    if r in 'Nn':
        break

for p in pessoas:
    if p[1] == maior_peso:
        mais_pesados.append(p[0])
    if p[1] == menor_peso:
        mais_leves.append(p[0])

print(f'Pessoas cadastradas: {pessoas}')
print(f'foram cadastradas {len(pessoas)} pessoas!')
print(f'Lista das pessoas mais pesadas pesando {maior_peso}: {mais_pesados}')
print(f'lista das pessoas mais leves pesando {menor_peso}:  {mais_leves}')