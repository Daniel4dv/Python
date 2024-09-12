import modulo
import importlib 

print(modulo.nome)

for i in range(10):
    importlib.reload(modulo) #recararega o modulo para ser executado varias vezes
    print(i)