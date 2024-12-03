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
    b = {}
    b['Quantidade de notas'] = len(notas)
    b['Maior nota'] = max(notas)
    b['Menor nota'] = min(notas)
    b['Media da turma'] = sum(notas)/b['Quantidade de notas']
    if sit:
        b['Status'] = 'BOA' if  b['Media da turma']>6 else 'RUIM'
    return b


print(boletim(0,5,7.5,4,2,4.5,sit=True))

help(boletim)


    
      