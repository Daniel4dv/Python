pessoa = {
    'nome': 'Daniel',
    'sobrenome': 'Felipe'
}

def insere(**kwargs):
    return kwargs

(a1 ,a2),(b1,b2) = pessoa.items()



pessoa['idade'] = None
for chave,valor in pessoa.items():
    print(chave,valor)
    
outro = {'pessoas': pessoa}

pessoa2 = {**pessoa,'endereco':'rua A n 50'} # Adicionando um dict como conteudo de dict empacotando ele
print(pessoa2)