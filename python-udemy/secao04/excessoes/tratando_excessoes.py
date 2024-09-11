# TRY,EXCEPT,ELSE,FINALLY
try:
    a = 19
    b = int(input('dividir 19 por: '))
    c = a/b
    print(c)
except ZeroDivisionError:
    print('Nao da pra dividir por zero')
except TypeError:
    print('Digite um valor numérico')
except ValueError as erro: ## classe do erro as instancia do erro
    print('Erro:', erro.__class__.__name__)  ## Nome da classe da instancia do erro
    print('Digite um valor válido')
except NameError:
    print('O valor de divisão precisa ser digitado')
except Exception as erroDesconhecido:
    print('Erro:',erroDesconhecido.__class__.__name__)
    print('Erro desconhecido')
else:
    print('è executado apenas se não houver erros no codigo!') #Como um else de except
finally:
    print('Fechar o arquivo')  #Ocoprrendo excessões ou não, o finally será executado, podendo finalizar ações em casos de erro ou não

#não é possivel usar o try sozinho ou o try:else


exit()
try:
    print(1)
finally:
    print(10)