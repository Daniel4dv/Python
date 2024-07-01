# interpolarização de strings, armazenando letras em strings

nome ='luis otavio'

tam = len(nome)
ind = 0
nome2=''
while ind <tam:
    letra = (nome[ind])
    nome2 += f'+{letra}'
    ind+=1

print(nome2)
