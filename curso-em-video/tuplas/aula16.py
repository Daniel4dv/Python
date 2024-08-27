lanche = 'Hamburguer',"suco",'Pizza','Pudim'

print(lanche[-1])
print(lanche[0:2])

for cont in range(len(lanche)):
    print(lanche[cont])

    #ou

for lanc in lanche:
    print(lanc)

# obtendo o dado numeral com a var composta

for pos, lanc in enumerate(lanche):
    print(f'O item {pos} é {lanc}.')

    # concatenando tuplas
a = (1,2,3,4)
b = (5,6,7,8)
c = a + b
print(c)
#metodos com funcoes
print(c.count(4)) #nome da lista.count conta quantas vezes o valor aparece na lista
print(c.index(8)) #nome da lista.index mostra em que posicao esta o item em questao, na primeira ocorrencia, caso queira identiifcar a 2 coloque,pos
print(c)
del(c) # deleta a tupla completamente