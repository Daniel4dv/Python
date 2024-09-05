palavra = set('garrafa')
print(palavra)
tried = set()

while True:
    l = input('Digite: ')
    if l in palavra:
        tried.add(l)
    print(tried)
    if tried == palavra:
        print('Voce ganhou!')
        print('Palavra secreta: Garafa')