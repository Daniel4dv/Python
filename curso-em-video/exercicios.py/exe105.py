def boletim(*args,sit=False):
    '''
    FUNCAO BOLETIM
    PARAMETROS:
    args = coleta quantas notas forem necessarias
    sit= parametro opcional para exibir sit da turma
    '''
    notas = list(args)
    print(f'Notas: {notas}')
    print()
    conclusao = {}
    conclusao['Quantidade de notas'] = len(notas)
    conclusao['Maior nota'] = max(notas)
    conclusao['Menor nota'] = min(notas)
    conclusao['Media da turma'] = sum(notas)/conclusao['Quantidade de notas']
    if sit:
        conclusao['Status'] = 'BOA' if  conclusao['Media da turma']>6 else 'RUIM'
    return conclusao


print(boletim(10,5,7.5,4,2,4.5,sit=True))

help(boletim)


    
      