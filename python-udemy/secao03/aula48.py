# TRY AND EXCEPT  (TIPO IF E ELSE)


# print(numero_str.isdigit()) #digit string = string SO com numeros

numero_str=input('Dobrar:')


# if numero_str.isdigit():
#     print(f'Voce digitou {numero_str}')
#     numerof = float(numero_str)
#     print(f'O dobro de {numero_str} é {numerof*2:.0f}')
# else:
#     print('digite um numero valido!')


try:
     print(f'Voce digitou {numero_str}')
     numerof = float(numero_str)
     print(f'O dobro de {numero_str} é {numerof*2:.0f}')   
except:
     print('digite um numero valido!')