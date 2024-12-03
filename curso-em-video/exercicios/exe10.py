din=float(input("Quanto você tem pra gastar?\n"))
dol=din/4.94
euro=din/5.27
print()
print("Você connsegue comprar {:.2f} dólares".format(dol))
print("OU")
print("com R${}, você pode comprar {:.2f} euros".format(din,euro))
