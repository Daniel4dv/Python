from datetime import datetime
ficha = {}

ficha['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
ficha['idade'] = datetime.now().year - nascimento
ficha['ctps'] = int(input('CTPS [0 - NÃO TENHO]: '))

if ficha['ctps'] != 0:
    ficha['ano'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: '))
    ficha['aposentadoria'] = ( ficha['ano'] + 35) - nascimento

print(ficha)

for k,v in ficha.items():
    print(f'{k}: {v}')

