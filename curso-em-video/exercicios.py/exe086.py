matriz = [[0,0,0], [0,0,0], [0,0,0] ]
for i in range (3):
    for j in range(3):
       matriz[i][j] = int(input(f'Digite o valor [{i,j}]: '))
       

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^3}]', end='')
    print()

# print(f'[{matriz[0][0]:^3}] [{matriz[0 ][1]:^3}] [{matriz[0 ][2]:^3}]')
# print(f'[{matriz[1 ][0]:^3}] [{matriz[1 ][1]:^3}] [{matriz[1 ][2]:^3}]')
# print(f'[{matriz[2 ][0]:^3}] [{matriz[2 ][1]:^3}] [{matriz[2 ][2]:^3}]')


# deu bom fml