from math import radians, sin, cos, tan
ang = int(input("digite o angulo: "))
sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))

print()
print("O seno de {} é {:.2f}".format(ang, sen))
print("O cosseno de {} é {:.2f}".format(ang, cos))
print(" A tangente de {} é {:.2f}".format(ang, tang))
