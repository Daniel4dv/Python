import random
print("Digite o nome dos alunos...")
print()
a1=input("1º aluno: ")
a2=input("2º aluno: ")
a3=input("3º aluno: ")
a4=input("4º aluno: ")

ordem=[a1,a2,a3,a4]
random.shuffle(ordem)
print()
print(ordem)