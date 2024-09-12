# Verificacao de tipo de dados em massa

lista = [
    'a',1,2,True,(5,7,0),{'pedro','joao'},
    {'chave':'valor'},5.7
]

for item in lista:
    if isinstance(item,set):
        item.add(5)
        print('SET')
        print(item)

for item in lista:
    if isinstance(item,str):
        print('STR:')
        print(item.upper()) #STRINGS SAO IMUTAVEIS, LOGO ESTAMOS APENAS 
                                    # EXIBINDO COM UPPER

print('INT,FLOAT:')
for item in lista:
    if isinstance(item,(int,float)):
        print(item,isinstance(item,(int,float)))


print(lista)
    
    
