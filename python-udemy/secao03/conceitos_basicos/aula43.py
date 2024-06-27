
# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'daniel'
print(nome[0])
print('a' in nome) # verifica se a esta em nome
print ('x' not in nome)


print('-' *10)
nome=input('Digite seun nome:')
encontrar = input('Digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} existe em {nome}')
else:
    print(f'{encontrar} não existe em {nome}')

