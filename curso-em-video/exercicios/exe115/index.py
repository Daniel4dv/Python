from exe115.lib.interface import *
import os
from time import sleep

arq = 'cadastro.txt'

# if arquivo.arqExiste(arq):
#     print('ok')
# else:
#     print('nada ok')



while True:
    menu(["Ver pessoas cadastradas","Cadastrar pessoas","Sair do sistema"])
    op = leiaint()
    
    match op:
        case 1:
            print(cabecalho("Voce escolheu 1"))
            break
        case 2:
            print(("Voce escolheu 2"))
            break
        case 3:
            print(("Voce escolheu 3"))
            encerramento()
            break
        case default:
            os.system('cls')
            sleep(.5)
            print("\033[31mOpção inválida! Tente novamente\033[0m")
            sleep(.5)

            



    


