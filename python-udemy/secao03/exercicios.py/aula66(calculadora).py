print('=-'*20)
print('         CALCULADORA')
print('=-'*20)
while True:
    n1 = input('Digite o primeiro numero:')
    n2 = input('Digite o segundo numero:')

    nmr_validos = None

    try:
        n1 = float(n1)
        n2 = float(n2)
        nmr_validos = True
    except ValueError:
        nmr_validos = None
    
    if nmr_validos is None:
        print('=-'*20)
        print("Digite números válidos!")
        print('=-'*20)
        continue

    

    print('O que deseja calcular?')
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')
    op =input('>')

    try:
       if op not in '1 2 3 4':
           print('Digite uma opção valida')
           continue
       op = int(op)

    except ValueError:
        print('Digite uma opção válida')
        continue

    resultado = 0
    if op == 1:
        resultado = n1+n2
    elif op==2:
        resultado = n1-n2 
    elif op == 3:
        resultado = n1*n2
    elif op==4:
        resultado=n1/n2

    print(f'resultado: {resultado}')

    print('Deseja sair do programa?')
    sair = input('[s]im [n]ão:').lower().startswith('s') # funções para dar lower no texto, e verificação de começa com('x')? que retorna bool
    if sair is True:
        print('Voce saiu do programa!')
        break

