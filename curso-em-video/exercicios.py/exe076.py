tupla = ('Capacete',75.99,\
    'Meia',49.99,\
    'Tenis',89,\
    'Bracelete',370.99)
    
i = int(0)
print('-'*35)
print(f"{'TABELA DE PREÇOS':^35}")
print('-'*35)
for i in range(0,len(tupla),2):
    print(f'{tupla[i]:.<30} R${tupla[i+1]:>7.2f}')


# CONCLUIDO 