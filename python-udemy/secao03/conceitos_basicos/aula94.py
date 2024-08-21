salas =  [
    
    ['Joao', 'daniel']  ,
    ['maria','Helena'],
    ['Ela','Ele','Elu',(0,10,20,30)],

]

for sala in salas:
    print(sala[0])

print(*salas, sep='\n') #exibe todos os itens da lista * sep quebra as linhas em cada item