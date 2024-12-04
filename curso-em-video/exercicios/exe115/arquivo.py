import os
import modulos

# print(os.getcwd())
os.chdir(os.path.dirname(__file__))


def arquivoExiste(nome_arquivo):
   
    try:
        open(nome_arquivo,'r')
        print("Arquivo encontrado com sucesso!")       
    except Exception as erro:
        print(f"Erro:{erro}")
        
def criararquivo(nome_arquivo):
    try:
        a = open(nome_arquivo,'wt+')
        a.close()
    except:
        print("Houve um Erro na criaçao do documento")
    else:
        print(f"Arquivo {nome_arquivo} criado com sucesso")

def lerArquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rt') as arq:
            # Cabeçalho colorido
            modulos.cabecalho("\033[1;34m" + "PESSOAS CADASTRADAS" + "\033[0m")  # Azul para o cabeçalho
            
            
            # Exibindo o cabeçalho das colunas
            modulos.cabecalho(f"\033[32m{'Nome':<20}\033[0m \033[33m{'Idade':>5}\033[0m")  # Cabeçalho das colunas
            

            # Imprimindo os dados
            for linha in arq:
                dado = linha.strip().split(';')  # Remover espaços em branco e dividir os dados
                nome = dado[0]
                idade = dado[1]
                # Exibindo cada dado de maneira formatada, alinhando com as colunas
                print(f"\033[32m{nome:<20}\033[0m \033[33m{idade:>5}\033[0m")
            
            print("-" * 50)  # Linha separadora final

    except Exception as erro:
        print(f"\033[31mErro ao ler o arquivo: {erro}\033[0m")  # Mensagem de erro em vermelho
    finally:
        if 'arq' in locals():  # Verifica se o arquivo foi aberto para fechá-lo
            arq.close()




def cadastrar(nome_arquivo,nome='desconhecido',idade=0):
    try:
        with open(nome_arquivo,'at') as arq:
            arq.write(f'{nome};{idade}')
            print("\033[32m" + f"{nome} cadastrado com sucesso!" + "\033[0m")
    except:
        print("Houve um erro")