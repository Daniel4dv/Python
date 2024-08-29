boletim =[]
ficha = []

while True:


    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = float ((nota1+nota2) / 2)

    ficha.append(nome)
    ficha.append([nota1,nota2])
    ficha.append(media)
    print(ficha)
    boletim.append(ficha[:])
    ficha.clear()

    print('1 - Cadastrar outro aluno')
    print('2 - Mostrar média dos alunos')
    r = int(input('>'))

    if r == 2:
        break


print('=-'*15)
print(f'{"MÉDIA DOS ALUNOS":^30}')
print('=-'*15)
for i,a in enumerate(boletim):
    print(f'{i+1} - {a[0]:<10} : {a[2]:>10.2f}')

c=1
while c!= 0 :
    c = int(input('deseja consultar as notas de qual aluno? [0 - encerrar]'))
    if c is not 0:
        print(f'Notas do {boletim[c-1][0]} : {boletim[c-1][1]}')
print('PROGRAMA ENCERRADO')


