produto = {
    'nome': 'Caneta Azul',
    'preco': 2.50,
    'categoria': 'Escritorio'
}

lista = [
    ('chave','valor'),
    ('chave2','valor2'),
    ('chave3','valor3')
]

dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor  #usando mapeamento com upper()
    for chave,valor
    in produto.items()
    if not isinstance(valor,(int,float)) or valor > 3 #filtrando por preco
    
}
dc_lista = {
    chave:valor 
    for chave,valor in lista 
}

print(dc_lista)