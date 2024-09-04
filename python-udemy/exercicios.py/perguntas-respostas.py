perguntas = [
    {
        'pergunta':'Quais destes números não é primo?',
        'opcoes': [1,3,7,12],
        'resposta':4
    },
    {  
        'pergunta': 'Quem descobriu o Brasil?',
        'opcoes': ['Pedro Alvares Cabral','Fausto Silveira','Elon Musk','Monark do Flow'],
        'resposta': 1
    },

    {  
        'pergunta': 'Quanto custa o KG do peso de 10kg',
        'opcoes': ['5.99/kg','12,99/kg','A unidade','Mais do que o de 5kg'],
        'resposta': 3
    },
]

print('=-'*30)
print(f'{"JOGO DE PERGUNTAS E RESPOSTAS":^60}')
print('=-'*30)

respostas = []

for i,p in enumerate(perguntas):
    print(f'<<<<    PERGUNTA {i+1}  >>>>')
    print(perguntas[i]['pergunta'])
    for j,op in enumerate(perguntas[i]['opcoes']):
        print(f'{j+1}) {op}')
    while True:
        r = input('Sua resposta: ')
        if r.isdigit():
            r = int(r)
            if r>4 or r<1:
                print('Opção inválida. Tente novamente')
            else:
                respostas.append(r)
                if r != perguntas[i]['resposta']:
                    print('Você ERROU ❌')
                    print()
                else:
                    print('Você ACERTOU ✅')
                    print()
                break
        else:
            print('Valor inválido')

acertos = 0
for q in range(3):
    if respostas[q] != perguntas[q]['resposta']:
        print(f'A pergunta {q+1} você ERROU ❌')
        print(f'A resposta certa era "{perguntas[q]["opcoes"][perguntas[q]["resposta"]-1]}"')
    else:
        print(f'A pergunta {q+1} você ACERTOU ✅')
        acertos+=1
        
    print('=-'*15)


print(f'NOTA : {acertos}/{len(perguntas)}')
print(respostas)