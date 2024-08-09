lista_a =['maria', 'luiz']
lista_b = lista_a
# lista_b = lista_a.copy()  .copy() salva uma copia basica ao inves de apontar para o valor



print(lista_b)  #valores mutaveis apontam para valores como ponteiros em C, FAZENDO COM QUE as alteraçoes se mantenham na lista_b por exemplo

i = 1
for nome in lista_b:
    print(f'{i} - {nome}')
    i+=1 

