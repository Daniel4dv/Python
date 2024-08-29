boletim = []
aluno = []
while True:

    nome = input('Digite o nome do aluno: ')
    nota1 = int(input('Digite a primeira nota do aluno'))
    nota2 = int(input('Digite a segunda nota do aluno'))
    for i in range(10):
        aluno.append(nome,nota1,nota2)

    r = int(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break

print(aluno)
