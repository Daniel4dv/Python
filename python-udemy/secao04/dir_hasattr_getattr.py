#dir /hasattr /getattr

string = 'Daniel Junio      '
maiusculo = 'uper'
minusculo = 'lower'
tira_espacos = 'strip'

if hasattr(string,maiusculo):  #verifica se ha um metodo especifico em um dado
    print('Existe upper')
    print(getattr(string, maiusculo)()) # coleta uma resultado a partir de (dado,metodo)

if hasattr(string,minusculo):
    # print('Existe upper')
    print(getattr(string, minusculo)(),'OK')

if hasattr(string,tira_espacos):
    # print('Existe upper')
    print(getattr(string, tira_espacos)(),'OK')


