'''
160.805.716-09
16080571609

10 - 9 - 8 - 7 - 6 - 5 - 4 - 3 - 2 - 1 
1    3   1   2   3   4   6   6   6   multiplicar
10   27  8   14  18  20  24  18  12  =  188

resultado * 10
1880

obter resto da divisão/mod/% por 11
10

com esse resultado tem se a seguinte resposta
se maior que nove = 0
se 9 ou menor = resultado original(2)
  
com isso temos 160.805.716-0...

'''

cpf = input('Digite seu cfp:')
nove_digitos = cpf[:9]
numero_multiplicador = 10
soma_valores = 0

print(type(nove_digitos))
print(type(numero_multiplicador))
print(type(soma_valores))

for digito in nove_digitos:

    multiplicação = int(digito) * numero_multiplicador
    numero_multiplicador-= 1
    soma_valores = multiplicação + soma_valores

print(soma_valores)
soma_valores= (soma_valores*10)%11
print(soma_valores)

digito1 = 0
if soma_valores >9:
    digito1 = 0
else:
    digito1 = soma_valores

print(digito1)


'''
11 - 10 - 9 - 8 - 7 - 6 - 5 - 4 - 3 - 2 
1     6   0 . 8   0   5 . 7   1   6 - 0 (primeiro digito) ...  multiplicar
11   60   0   64   0  30  35  4   18  0 = 

'''


dez_digitos = nove_digitos + str(digito1)
print(dez_digitos)

soma_valores = 0
numero_multiplicador = 11

for digito in dez_digitos:
    multiplicação = int(digito) * numero_multiplicador
    numero_multiplicador-= 1
    soma_valores = multiplicação + soma_valores


print(soma_valores)
soma_valores = (soma_valores*10)%11
print(soma_valores)

digito2 = 0
if soma_valores >9:
    digito2 = 0
else:
    digito2 = soma_valores

print(digito2)
print("conclusão:")

print(digito1,digito2)
dois_digitos = str(digito1) + str(digito2)
print(dois_digitos)

print(cpf[9:11])
if dois_digitos == cpf[9:11]:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')

