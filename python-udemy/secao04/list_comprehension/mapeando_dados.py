#Gerando uma lista nova a partir de uma, possibilitando alterar dados de preferencia

#lista padrao
produtos = [
    {'nome':'p1','preco':50},
    {'nome':'p2','preco':30},
    {'nome':'p3','preco':20}
]

# Lista nova
produtos_novo = [
    {**produto,'preco':produto['preco']*1.5     #**produto desempacotado do valor original
     } if produto['preco'] > 20 else {**produto}
     for produto in produtos 

]

print(*produtos,sep='\n')
print('=-'*30) # comparando as listas
print(*produtos_novo,sep='\n')



