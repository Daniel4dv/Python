# FORMATAÇÃO

nome = 'daniel'
peso = 62.5
altura = 1.75 # imc = peso/(altura*2)
imc = peso / altura**2

linha =f'{nome} tem {altura} de altura, pesa {peso:} então seu IMC é {imc:.2f}' 
print (linha)