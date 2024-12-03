def leiaint():
    while True:
        try:
            n = input("Digite um numero inteiro:")
            n = int(n)
            break
        except Exception as erro:
            print(f'Numero invalido. Tente novamente! ({erro.__class__})')
            continue

def leiafloat():
    while True:
        try:
            n = input("Digite um numero float:")
            n = float(n)
            break
        except Exception as erro:
            print(f"Numero invalido.Tente novamente! ({erro.__class__})")
            continue



leiaint()
leiafloat()
