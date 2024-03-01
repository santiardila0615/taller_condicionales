#programa para calcular en que cuadrante esta un punto,de un plano cartesiano 

#entrada 
X = int(input("ingresa la coordenada X:"))
Y = int(input("ignresa la coordenada Y:")) 

#proceso y salida
if X==0:
    if Y==0:
        print("La coordenada" , (X , Y),"esta en, el origen")
    else:
        print("la  coordenada" ,( X , Y),"esta en el el eje Y")
elif Y==0:
    print("la  coordenada" ,(X , Y),"esta en el el eje X")
elif X>0:
    if Y>0:
        print("La coordenada" ,(X , Y),"esta en el cuadrante 1")
    else:
        print("La coordenada" ,(X , Y),"esta en el cuadrante 4")
elif Y<0:
    print("La coordenada" ,(X , Y),"esta en el  cuadrante 3")
else:
    print("La coordenada" ,(X , Y),"esta en el cuadrante 2")