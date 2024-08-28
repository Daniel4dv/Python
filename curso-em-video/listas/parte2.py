galera = []
dado = []

for i in range(3):
    dado.append(input('Nome:'))
    dado.append(input('Idade:'))
    galera.append(dado[:])
    dado.clear()

print(galera)

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




