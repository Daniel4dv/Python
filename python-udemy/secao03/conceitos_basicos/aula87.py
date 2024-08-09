#DESEMPACOTAMENTO

nomes = ['maria','joao','daniel','luis','mariana']  #vamos desempacotar essa lista

nome1,*resto = nomes  # *determina que a var armazenara mais de um valor nesse tipo de comando (sendo uma lista)

print(nome1) #perceba que nome1 funciona normalmente
print(resto) # e que resto armazena todos os outros valores restantes da lista   

_,_, nome3, *_ = nomes

print(_)