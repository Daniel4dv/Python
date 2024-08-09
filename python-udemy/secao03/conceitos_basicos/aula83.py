lista_a = [1,2,3]
lista_b = [4,5,6]

lista_c = lista_a + lista_b #concatenação armazenada em outra variavel
print(lista_c)

lista_a.extend(lista_b)  #nao retorna nada, apenas manipula um valor ao valor que recebeu a função/metodo

print(lista_a)
