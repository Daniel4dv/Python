#FILTRANDO DADOS DE UMA LISTA PRA INSERIR NA OUTRA APENAS SE QUISER

import pprint
#lista padrao
produtos = [
    {'nome':'p1','preco':50},
    {'nome':'p2','preco':30},
    {'nome':'p3','preco':20}
]

# Lista nova
produtos_novo = [
    {**produto,'preco':produto['preco']*1.5    
     } if produto['preco'] > 20 else {**produto}
     for produto in produtos 
    if produto['preco'] < 40
]

# lista = [n for n in range(10)  #cria uma lista com filtro, apenas inserindo os dados
#          if n<6                 # que atendem os requisitos
#          ]                
# print(lista)




# print(produtos_novo)
pprint.pprint(produtos_novo)  #IDEAL PARA EXIBIR DADOS COMPLEXOS
