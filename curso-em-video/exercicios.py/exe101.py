from datetime import datetime
idade = 0
def voto(nasc):
    if nasc !=0:
        resultado = 'NEGADO'
        ano_atual =  datetime.now().year
        global idade
        idade = ano_atual - nasc
        if idade>=18 and idade <60:
            resultado = 'OBRIGATÓRIO'
        elif idade> 16 or idade>60:
            resultado = 'OPCIONAL'
        return resultado


while True:    
    ano = int(input('Em que ano voce nasceu: '))
    status = voto(ano)
    if ano ==0:
        break
    print(f'Com {idade} anos, seu voto é {status}')


