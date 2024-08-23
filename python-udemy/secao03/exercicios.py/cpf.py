cpf = input('Digite seu cfp:')
nove_digitos = cpf[:9]
numero_multiplicador = 10
soma_valores = 0

for digito in nove_digitos:

    multiplicação = int(digito) * numero_multiplicador
    numero_multiplicador-= 1
    soma_valores = multiplicação + soma_valores

soma_valores= (soma_valores*10)%11


digito1 = 0
if soma_valores >9:
    digito1 = 0
else:
    digito1 = soma_valores


dez_digitos = nove_digitos + str(digito1)

soma_valores = 0
numero_multiplicador = 11

for digito in dez_digitos:
    multiplicação = int(digito) * numero_multiplicador
    numero_multiplicador-= 1
    soma_valores = multiplicação + soma_valores

soma_valores = (soma_valores*10)%11

digito2 = 0
if soma_valores >9:
    digito2 = 0
else:
    digito2 = soma_valores

cpf_calculo = f'{nove_digitos}{digito1}{digito2}'



print('CPF VÁLIDO' if cpf==cpf_calculo else 'CPF INVÁLIDO')
