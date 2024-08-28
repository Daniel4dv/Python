
def conta(quantidade):
    def numero(n):
        return f'{n} * {quantidade} = {n *quantidade}'
    return numero()

duplicar = conta(2)
triplicar = conta(3)
quadruplicar = conta(4)

print(duplicar(5))
print(triplicar(5))
print(quadruplicar(5))