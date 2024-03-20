from math import *
#entrada
a = float(input("ingrese el primer coeficiente:"))
b = float(input("ingrese el segundo coeficiente:"))
c = float(input("ingrese el tercer coeficiente:"))

# entrada
if a == 0:
    print("no es una ecuacion cuadratica")
else:
    d = b**2-4*a*c
    if d == 0:
        x1 = -b/(2*a)
        x2 = x1
        print("los resultados son x1=", str(x1), "y x2=", str(x2))
    elif d > 0:
        x1 = (-b+sqrt(d))/(2*a)
        x2 = (-b-sqrt(d))/(2*a)
        print("los resultados son x1=", str(x1), "y x2=", str(x2))
    else:
        print("no hay solucion real")