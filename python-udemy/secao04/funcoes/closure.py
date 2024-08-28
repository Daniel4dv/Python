'''
closure
'''
def saudacao(s):
    def saudar(nome): # parametro nome e definido apenas nas segunda funcao, nao sendo necessario nome na hora de invocar a funcao saudacao
        return f'{s}, {nome}!' #retorno final da funcao, com os valores sendo exibidos
    return saudar   #usando sem parenteses voce retorna a funcao ao inves de retornar o valor da funcao, armazenando a funcao na variavel 
                    #ao inves do valor

s1 = saudacao('bom dia')
s2 = saudacao('Boa noite')
s3 = saudacao('Bem vindo')

''' Os funcoes estao sendo salvas nas variaveis com o cache dos parametros designados podendo fazer o closure () quando quiser'''

print(s1('Daniel')) #executando a funcao saudacao(s1) com o parametro nome definido apenas agora ja que a definição do mesmo era opcional antes
print(s3())
