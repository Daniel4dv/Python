import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except Exception as erro:
    print("O site nao esta acessivel no momento", erro.__class__)
else:
    print("tudo ok")