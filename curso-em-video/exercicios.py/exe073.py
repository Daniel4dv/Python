tabela = ('Fortaleza','Botafogo','Palmeiras','Flamengo','São Paulo','Bahia','Cruzeiro','Vasco','Atlético-MG','Athletico-PR','Internacional',\
'Juventude','Grêmio', 'Bragantino' ,'Criciúma','Fluminense','Vitória','Corinthians','Cuiabá','Atlético-GO')

print('=-'*30)
print('Os 5 primeiros colocados da tabela:')
print(tabela[0:5])
print('=-'*30)
print("Os ultimos 4 colocados da tabela")
print(tabela[-4:])  # ultimo item nao conta
print('=-'*30)
print('Times da tabela em ordem alfabetica:')
print(sorted(tabela))
print('=-'*30)
print('Em que posição o cruzeiro está?')
print(tabela.index('Cruzeiro')+1,'ª posição')
print('=-'*30)

