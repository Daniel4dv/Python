def arqExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return False
    else:
        return True