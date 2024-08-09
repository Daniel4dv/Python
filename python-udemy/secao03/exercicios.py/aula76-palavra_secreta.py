import os

palavra = 'desodorante'
letras_acertadas = ''
palavra_formatada = '_ _ _ _ _ _ _ _ _ _ _'

print(palavra_formatada )
erros = 0
while True:
    letra = input('Digite uma letra:')

    if len(letra)> 1:
        print('Digite apenas uma letra')
        continue

    

    if letra in palavra:
        letras_acertadas += letra
    else:
        erros += 1
   

    palvra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palvra_formada += letra_secreta
        else:
            palvra_formada += ' _ '
    print(palvra_formada)

    if palvra_formada == palavra:
        os.system('cls')
        print('Você Ganhou!')
        print(f'A palavra era {palavra}')
        print(f'erros: {erros}')
        erros=0
        letras_acertadas=''
        continue
        