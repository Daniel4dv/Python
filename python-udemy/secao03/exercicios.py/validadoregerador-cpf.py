import re
import sys
import random

while True:
    print('O que deseja fazer?')
    print('1 - Validar um CPF')
    print('2 - Gerar um CPF')
    op = input('>')

    if int(op) == 2:
        # gerador de cpf
        soma_valores = 0

        # nove_digitos = str(random.randint(0,999999999))
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0,9))

        print(nove_digitos)
        numero_multiplicador = 10
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

            

        # digito2

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

        

        cpf_gerado = f'{nove_digitos}{digito1}{digito2}'
        print(f'CPF: {cpf_gerado}')

        print('Voltar ao menu?')
        print('1 - Sim')
        print('2 - Não (encerrar programa)')
        op2 = input('>')
        if op2==2:
            break

    elif int(op) == 1:
    # Validador de CPF
        
        cpf = input('Digite seu cfp:')\
            .replace('-','')\
            .replace('.','')

        if cpf[0]*len(cpf) == cpf:
            print('CPF INVÁLIDO')
            sys.exit()  # aborta o sistema

        # usando replace para limpar a string do cpf
        #  ex: 152.709.330-12(tirar pontos e barras)
        # ///
        # usando expressao regular para limpar o cpf
        cpf2 = re.sub(
            r'[^0-9]',  #troque tudo aquilo que nao for um numero de 0 a 9
            '',     #troque por '' nada
            '110.035.510-33'
        )

        nove_digitos = cpf[:9]

        numero_multiplicador = 10
        soma_valores = 0

        # usando replace para limpar a string do cpf
        #  ex: 152.709.330-12
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


        if cpf != cpf_calculo:  # verificação de digitos repetidos comomfalha do sistema fixada
            print('CPF INVÁLIDO')
        else:
            print('CPF VÁLIDO')

        print('Voltar ao menu?')
        print('1 - Sim')
        print('2 -  Não (encerrar programa)')
        op2 = input('>')
        if op2==2:
            break
