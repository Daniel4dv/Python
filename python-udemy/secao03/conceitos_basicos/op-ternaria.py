# print ('Verdade' if True else 'Falso') #modo mais pratico e dinamico de usar um if else 

digito = 10
digito_corrigido = 0 if digito > 9 else digito

print(digito_corrigido)

print('teste:')
print('valor1' if False else "valor2" if False else "Valor3")

if False:
    print("Valor1")
elif False:
    print('valor2')
elif True:
    print('valor3')
elif False:
    print('valor4')