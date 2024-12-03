aluno = {}

aluno['nome'] = str(input('Digite seu nome: '))
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))

aluno ['status'] = 'APROVADO' if aluno['media'] > 6 else 'RECUPERÇÃO' if aluno['media']> 4 else 'REPROVADO'

for k,v in aluno.items():
    print(f'{k}: {v}')


