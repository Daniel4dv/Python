def cab(titulo):
    print('=-'*20)
    print(f'{titulo:^40}')
    print('=-'*20)

cab('Curso Python')


# empacotamento d4 param,etrosd args aquele ngc loco la ce ja sabe akakakakaw

def contador(*args): #se passar 1 parametro ok se passar 500 ok tbm kkkkkk
    print(sum(args))

contador(1,4)

def dobra(lista):
   pos = 0
   while pos< len(lista):
        lista[pos] *= 2
        pos += 1


numeros = [1,2,3,5,8,9]
dobra(numeros)
print(numeros)