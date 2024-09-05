s1 = set('luiz')  # {'l', 'u', 'i', 'z'}
s1.add('luiz')    # {'l', 'u', 'i', 'z', 'luiz'}
print(s1)         # {'l', 'u', 'i', 'z', 'luiz'}

s1.update('daniel')  #pode passar mais de um valor por vez
print(s1)      

#Limpando o set
# s1.clear()
# print(s1)

#limpar elemento especifico (sem indice)
s1.discard('l') # remove o 'l' do set
print(s1)