#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   MANIPULAÇÃO DE STRINGSS    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

frase = " Dou o Cu Mesmo De Acordo  "
print(frase[9::2]) # formatará o texto printando começando do 9ºcar:(indo ate o final pois é 0): de 2 em 2
print(len(frase)) #conta quantos caracteres possui a frase
print(frase.count("o",0,5)) #contar quantos "o" existem na frase, podendo fazer essa contagem em uma frase manipulada
print(frase.find("bunda")) #procurar por uma palavra que n existe retornará (-1)
print("cu" in frase) #existe esse str na frase? true or false?
print(frase.replace("o cu","a bunda")) #>>>> troca de caracteres
print(frase.upper()) #deixa tudo em letra maiúscula
print(frase.lower()) #deixa td minusculo
print(frase.capitalize()) #deixa td minusculo com excessão do 1º caractere
print(frase.title()) #deixa a inicial de cada palavra maiuscula
print(frase.strip()) #remove os espaços inúteis
print(frase.rstrip()) # remove apenas os ultimos espaços inuteis (right strip)
print(frase.lstrip()) # remove os espaços da esquierda( left strip)
frase.split() # reseta a indexação de cada palavra
palavras = frase.split()
junto = '%'.join(palavras)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    ESTRUTURA CONDICIONAL   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x=int(5)
if x==5: # com 2 pontos, n esquecer
    print("é 5")
else: # com 2 pontos, n esquecer
    print("n é 5")

    #biblioteca random é utillll

import random
x=random.randint(0,9)
print(x)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CONDIÇÕES ANINHADAS   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

x=float(4.5))
if x>5: # com 2 pontos, n esquecer
    print("maior q 5")
elif: x<4 # com 2 pontos, n esquecer
    print("menor q 4")
else:
    print("nem um nem outro")



# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<    CORES NO TERMINAL    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# estrutura
# \033[ <codigo da cor> m "" \033[m
# style: 0, 1, 4, 7
# text collor: 30,31,32,33,34,35,36,37
# backgroundf collor: 40,41,42,43,44,45,46,47
text                    background
 
30    black    |preto       40
31    red      |vermelho    41
32    green    |verde       42
33    yellow   |amarelo     43
34    blue     |azul        44
35    Magenta  |Magenta     45
36    cyan     |ciano       46
37    grey     |cinza       47
97    white    |branco      107

print("\033[34mOlá, Mundo!\033[m")
a = 4
b = 5
print("O valores são \033[4;32m{}\033[m e \033[4;31m{}\033[m".format(a, b))

# é possivel armazenar nome de cores em dicionarios,
# criando uma lista e associando o codigo de cada uma a elas
cores= {}
estrutura = "amarelo': '\033[35m"

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< conversão para binarios etc >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
binario bin(var1)
octal oct(var1)
hexadecimal hex(var1)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< repetições FOR>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

for <var1> in range(1,10,2): #numero de repetições,incremento
    <comando no loop>
<comando após loop>

#FORMULA PARA POSIÇÃO DE UMA P.A
i+(10-1)*inc

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  REPETÇÕES COM ENQUANTO  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
while <var> >= 5: #exemplo
    print("")
    <var>=<var>+1

x = 1
y=int(input(">"))
while x <= y:
    print(x, end=" ")
    x += 1
print("\n")
for c in range(1,y):
    print(c,end=" ")

r="s"
while r=="s":
    n=int(input("Digite um valor:"))
    r=str(input("Quer continuar? [S/N]:")).lower()
print("Fim")

n=1
while n!=0:
    n = int(input("Digite um valor:"))
print("Fim")

# <<<<<<<<<<<<<<<<<<<<<<    TUPLAS    >>>>>>>>>>>>>>>>>>>>>>>> VARIAVEIS COMPOSTAS
# TRATAMENTO DE LISTAS OU SEMELHANTE 

# ex: variavvel (lanche[0,1,2,3,4])
# podemos printar escolhendo o item da lista
lanche={1,2,3,4,5}
print(lanche[1]) # printa apenas o 1
print(lanche[0:3]) #de 0 ate 2
print(lanche[2:]) # ate o fina

# é possivel usar o for nessas listas de forma simpples
# ao inves de for in range(x,y)
# temos for in lanche

# tuplas sao imutaveis, nao permitindo alternar o valor durante o programa
# ex:
lanche = ('hamburguer','suco ','pizza','pudim')
print(lanche[:2])
for comida in lanche:
    print('eu vou comer {}'.format(comida))
# enumerando a lista com (enumerate)
    for pos,comida in enumerate(lanche):
    print("Eu vou comer {} na posição {}".format(comida,pos))
#comando sorted(organizar)
    print(sorted(lanche)) # printara a lista em ordem alfabetica
# comando count (contar)
    c = 1,2,3,4,4,5,5,6,6,6,7,8,9,9
    print(c.count(9)) # mostra quantas vezes o nmr 9 aparece em c
# comando index (indexar)
    print(c.index(4)) # mostra em que posição aparece o 4 pela primeira vez
#comando
    del(lanche) #appaga a variavel composta por completa


