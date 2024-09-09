c = (
    '\033[m',         # 0 - Sem cor (reset)
    '\033[0;30;41m',  # 1 - Texto preto com fundo vermelho
    '\033[0;30;42m',  # 2 - Texto preto com fundo verde
    '\033[0;30;44m',  # 3 - Texto preto com fundo azul
    '\033[0;30;46m',  # 4 - Texto preto com fundo ciano
    '\033[47m',  # 5 - Texto preto com fundo branco
    '\033[1;37;40m',  # 6 - Texto branco em fundo preto (negrito)
)


def ajuda(nome):
    titulo(f'Acessando comando {nome}...',3)
    print(c[0])
    print(c[5])
    help(nome)
    print(c[0])

def titulo(msg,cor = 0):
    tam = len(msg) +4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(c[0],end='')


while True:
    titulo('Sistema de ajuda PyHelp',cor=2)
    n = input('Digite a funcao ou biblioteca para consultar [s - sair]: ')
    if n.lower() == 's':
        print('<Volte Sempre>')
        break
    ajuda(n)
