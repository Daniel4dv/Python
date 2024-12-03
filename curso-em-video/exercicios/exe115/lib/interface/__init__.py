
def leiaint():
    while True:
        try:
            n = input(">")
            n = int(n)
            return n
        except Exception as erro:
            print(f'Numero invalido. Tente novamente! ({erro.__class__})')
            continue
        

def linha(tam=20):
    print('=-'*tam)

def cabecalho(txt):
    linha()
    print(txt.center(40))
    linha()
    
def menu(lista):
    cabecalho("Menu Principal")
    c = 1
    for item in lista:
        print(f"{c} - {item}")
        c+=1
    linha()


def encerramento():
    linha()
    print("Programa Encerrado. Ate logo!")
    linha()