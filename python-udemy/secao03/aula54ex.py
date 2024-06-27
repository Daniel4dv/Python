numero = input('Digite um numero inteiro:')


if numero.isdigit():
    numerof = int(numero)
    par = numerof %2 == 0
    if par:
        print('O numero que você digitou é par')
    else:
        print('O numero que você digitou é Ímpar')
else:
    print('Você precisa digitar um número inteiro!')


print('PROGRAMA 2')
hora = input('Digite quantas horas é agora:')
if hora.isdigit():
    hora = int(hora)
    dia = hora <12 and hora>0
    tarde = hora >=12
    noite = hora>=18

    if dia:
        print('Bom dia usuário!')
    if tarde:
        print('Bom tarde usuário!')
    if noite:
        print('Bom noite usuário!')
