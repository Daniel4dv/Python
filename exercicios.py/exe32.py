from datetime import date

ano=int(input("""Digite um ano qualquer, e te direi se ele foi,é ou sera BISSEXTO:
Digite 0 para analisar o ano atual:\n"""))
if ano == 0:
    ano = date.today().year 

if ano%4==0 and ano % 100 != 0 or ano % 400 == 0:
    print("{} é BISSEXTO".format(ano))
else:
    print("{} NÃO é BISSEXTO".format(ano))

    # CONCLUÍDO COM SUCESSO!
