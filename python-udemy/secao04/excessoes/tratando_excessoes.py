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
    print('O val or de divisão precisa ser digitado')
except Exception as erroDesconhecido:
    print('Erro:',erroDesconhecido.__class__.__name__)
    print('Erro desconhecido')
