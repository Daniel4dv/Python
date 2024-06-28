condicao = True
while condicao:
    print('1')
    print('2')
    print('3')
    print('voce quer parar?')
    op = input('1 - Sim 2 - Não: ')
    op = int(op)
    if op == 1:
        print('PROGRAMA ENCERRADO')
        break;


contador = 0
while contador <=100:
    contador = contador+1   
    if '4' in str(contador):
        print('não gosto de numero com 4')
        continue  #nao quebra o laço apenas reinincia com uma condição
    print(contador)
    
