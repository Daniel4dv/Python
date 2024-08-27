tupla = ('produto1','R$75,99',\
    'produto2','R$49,99',\
    'produto3','R$89,99',\
    'produto4','R$37,99')
    
i = int(0)
print('-'*35)
print("Tabela de preços:")
print('-'*35)
for i in range(0,len(tupla),2):
    print(f'{tupla[i]}....................{tupla[i+1]}')


# CONCLUIDO 