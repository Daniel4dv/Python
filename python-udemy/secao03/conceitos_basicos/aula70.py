frase = 'python e uma linguagem de programação ' \
'multiparadigma criada por GUIDP VAN NSEIOQ.  '\
'python é legal'

print(frase)

i = 0
qtd_apareceu = 0
letra_mais_apareceu = ''

while  i < len(frase):
    letra_atual = frase[i]
    apareceu_atual = frase.count(letra_atual) #conta a quantidade de algo em uma variavel
    
    i+=1


    if qtd_apareceu < apareceu_atual:
        if letra_atual!= ' ':
            qtd_apareceu = apareceu_atual
            letra_mais_apareceu = letra_atual

print(f'{letra_mais_apareceu=}, {qtd_apareceu=}')
