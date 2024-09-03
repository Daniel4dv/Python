 
pessoa = {}
cadastro = []
while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo:'))
    pessoa['idade'] = int(input('Idade:'))
    cadastro.append(pessoa.copy())

    r = int(input('Deseja continuar? \n'
                    '1 - sim \n'
                    '2 - Não \n'))
    if r==2:
        break

print(cadastro)
print('=-'*25)
print(f'Foram cadastradas {len(cadastro)} pessoas')
print('=-'*25)

total_idade = 0

for item in cadastro:
    total_idade += item['idade']
media_idade = total_idade/len(cadastro)


mulheres = []
idade_acima = []

for item in cadastro:
    if item['sexo'] in 'Ff':
        mulheres.append(item.copy())


for item in cadastro:
    if item['idade'] > media_idade:
        idade_acima.append(item.copy())

if idade_acima == None:
    idade_acima = str('Não se aplica')

print(f'Media de idade dos cadastrados: {media_idade:.0f}')
print('=-'*25)
print(f'Lista de mulheres:')

for m in mulheres:
    print("="*10)
    for k,v in m.items():
        print(f'{k}:{v}')

print('='*25)
print(f'Pessoas com idade acima da media:')
for a in idade_acima:
    print("=-"*10)
    for k,v in a.items():
        print(f'{k}:{v}')
