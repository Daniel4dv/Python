exp = input('Digite uma expressão matematica: ')
parenteses = []

for simb in exp:
    if simb == '(':
        parenteses.append(simb)
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(simb)
            break

print(parenteses)
if len(parenteses) == 0:
    print('A expressão esta correta')
else:
    print("A expressão esta inválida")
