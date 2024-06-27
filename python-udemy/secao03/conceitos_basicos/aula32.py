a= 'A'
b= 'B'
c= 'C'

string ='a={0},a={0},a={0},b={1},c={2}'
formato = string.format(a,b,c)

string ='a={0},a={0},a={0},b={1},c={letra3}'
formato = string.format(
    a,b,letra3=c) #parametro para arguentos, se nomear um precisa nomear os proximos



print(formato)