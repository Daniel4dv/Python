galera = []
dado = []

for i in range(3):
    dado.append(input('Nome:'))
    dado.append (int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()  # limpa uma lista

print(galera)
menores=[]
maiores = []
for p in galera:
    if p[1] >18:
        maiores.append(p)
    else:
        menores.append(p)

print(f'maiores de idade {maiores}')
print(f'Menores de idade {menores}')
exit()
teste = []

teste.append('Gustavo')
teste.append('40')

galera = []
galera.append(teste[:]) # com o [:] sinalizo que quero salvar uma copia negando qualquer ligação entre as listas
teste[0] = 'Daniel'
teste[1] = 22
galera.append(teste[:])

#dessa forma faço o backup das listas testes em galera fazendo com que eu salve tudo como desejado
print(galera)
print(f'A idade do daniel é {galera[1][1]}')




