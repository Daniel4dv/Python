total_idade = 0
pessoa = {}
cadastro = []
while True:
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo:'))
        if pessoa['sexo'] not in 'fFmM':
            print('Sexo inválido. Tente novamente!')
            print('=-'*20)
        else:
            break
    while True:
        pessoa['idade'] = input('Idade:')
        if pessoa['idade'].isdigit():
            pessoa['idade'] = int(pessoa['idade'])
            total_idade += pessoa['idade']
            break
        else:
            print('Idade invalida. Tente novamente!')
            print('=-'*20)

    cadastro.append(pessoa.copy())
    r = 0
    while True:
        r = input('Deseja continuar? \n'
                    '1 - sim \n'
                    '2 - Não \n')
        if r.isdigit():
            r = int(r)
        else:
            print('Valor inválido! Tente novamente.')
            print('=-'*20)
        if r==2 or r==1:
            break
        else:
            continue
    if r ==2:
        break
print(cadastro)
print('=-'*25)
print(f'Foram cadastradas {len(cadastro)} pessoas')
print('=-'*25)

mulheres = []
idade_acima = []

for item in cadastro:
    if item['sexo'] in 'Ff':
        mulheres.append(item['nome'])


for item in cadastro:
    if item['idade'] > total_idade/len(cadastro):
        idade_acima.append(item.copy())

if idade_acima == None:
    idade_acima = str('Não se aplica')

print(f'Media de idade dos cadastrados: {total_idade/len(cadastro):.0f}')
print('=-'*25)
print(f'Lista de mulheres:')

for m in mulheres:
    print(F'- {m}')

print('='*25)
print(f'Pessoas com idade acima da media:')
for a in idade_acima:
    print("="*20)
    for k,v in a.items():
        print(f'{k}:{v}')
