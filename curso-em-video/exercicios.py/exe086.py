matriz = [[0,0,0], [0,0,0], [0,0,0] ]
pares = 0
soma_ultima_coluna = 0

for i in range (3):
    for j in range(3):
       matriz[i][j] = int(input(f'Digite o valor [{i,j}]: '))
       if matriz[i][j] %2==0:
           pares += matriz[i][j]
        
maior_seg_linha = 0      
for i in range(3):
    for j in range(3):
        if j==2:
            soma_ultima_coluna += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior_seg_linha:
                maior_seg_linha = matriz[i][j]


print('=-'*25)
print(f'{"Matriz de dados:":^50}')
print('=-'*25)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end='')
    print()

print('=-'*25)
print(f'Soma dos valores pares: {pares}')
print(f'A soma dos itens da ultima coluna: {soma_ultima_coluna}')
print(f"O maior valor da segunda linha: {maior_seg_linha}")

# print(f'[{matriz[0][0]:^3}] [{matriz[0 ][1]:^3}] [{matriz[0 ][2]:^3}]')
# print(f'[{matriz[1 ][0]:^3}] [{matriz[1 ][1]:^3}] [{matriz[1 ][2]:^3}]')
# print(f'[{matriz[2 ][0]:^3}] [{matriz[2 ][1]:^3}] [{matriz[2 ][2]:^3}]')


# deu bom fml