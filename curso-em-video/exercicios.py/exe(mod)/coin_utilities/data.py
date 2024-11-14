def validar(q):
    while True:
        n = input(q)
        try:
            n = float(n.replace(',','.'))
            return n
        except ValueError:
            print('Digite um valor válido!')