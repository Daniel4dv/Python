pessoa  = {
    'nome': 'Daniel',
    'sobrenoms': 'Peixoto',
    'idade':16
}

if pessoa['idade']> 18:
    pessoa['cnh'] = 1234


cnh = pessoa.get('cnh','Não tem') #puxa um valor de uma chave e consegue atribuir um valor padrao no caso de None/Null 
print(cnh)
for i,v in pessoa.items():
    print(i,v)



#pop
#coleta o valor da chave e APAGA ela do dicionario
exit()
nome = pessoa.pop('nome')
print(pessoa)
print(nome)

# popitem  
# Basicamente a mesma coisa mas...
chave = pessoa.pop.item()  #remove a ultima chave do dict retornando uma tupla com key e value
print(chave) # -->> ('key','value')

#update
# atualiza e cria chaves no dicionario
#forma 1
pessoa.update(
    {'nome':'Camila',
     'peso':65.5}
)

#forma 2
pessoa.update(nome='camila',peso=65.5)

# forma3
tupla= (('nome','Novo nome'),('idade',15)),
pessoa.update(tupla)
print(pessoa)