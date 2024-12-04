import modulos
import arquivo
import os
from time import sleep




arquivo.arquivoExiste('cadastro.txt')


while True:
    modulos.menu(["Ver pessoas cadastradas","Cadastrar pessoas","Sair do sistema"])
    op = modulos.leiaint('Selecione uma opção:')
    
    match op:
        case 1:
            os.system('cls')
            arquivo.lerArquivo('cadastro.txt')
        case 2:
            modulos.cabecalho('NOVO CADASTRO')
            nome = str(input("Nome:"))
            idade = modulos.leiaint('Idade:') 
            arquivo.cadastrar('cadastro.txt',nome,idade)
        case 3:
            print(("Voce escolheu 3"))
            modulos.encerramento()
            break
        case default:
            os.system('cls')
            sleep(.5)
            print("\033[31mOpção inválida! Tente novamente\033[0m")
            sleep(.5)

            



    


