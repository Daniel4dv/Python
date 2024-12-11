cidades = ['Salvador','Ubatuba','Belo Horizonte']
estados = ['BA','SP','MG','RJ']


# for i in range(3):
#     print(f'{cidades[i]}, {estados[i]} ' )

def zipper(l1,l2):
    intervalo = min(len(l1),len(l2))
    return [
        (l1[i], l2[i]) for i in range (intervalo)
    ]

lista = zipper(cidades,estados)
print(lista)
print('-'*50)
print(list(zip(cidades,estados)))
print('-'*50)
# print(list(zip_longest(cidades,estados,fillvalue = 'Sem cidade')))    supostamente

# FUNCAO ZIP FAZ A MESMA COISA ZIP(L1,L2) RETORNANDO O ITERRATOR  (ZIP_LONGEST FAZ O MESMO MAS PRIORIZANDO A LISTA MAIOR)