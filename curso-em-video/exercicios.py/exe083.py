while True:
     
    expressão = input('Digite uma expressão qualquer: ')

    parenteses = [expressão[-2],expressão[-1]]
    print(parenteses)
    if parenteses[0]=='(' and parenteses[1] == ')':
        print('Os parenteses foram digitados corretamente')
    else:
        print('Os parenteses nao estao em ordem correta')