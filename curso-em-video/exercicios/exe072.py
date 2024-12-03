numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete',\
           'dezoito','dezenove','vinte')

while True:
    nmr = int(input('Digite um numero entre 0 e 20:'))
    if nmr >20 or nmr<0:
        print('Numero inválido.Tente novamente')
        continue
    else:
        print(numeros[nmr])
        continue

# CONCLUIDO
