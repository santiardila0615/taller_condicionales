import math 

#programa para calcular el precio de venta de diferentes productos en una papeleria

#input
precio_costo=int(input("por favor ingrese el precio de costo: "))

#processing

if precio_costo<3000:
    ganancia=precio_costo*0.15
elif precio_costo>6000:
    ganancia=precio_costo*0.25
else:
    ganancia=500

precio_venta=(ganancia + precio_costo)

#output
print ("el producto adquirido se debe vender a", + precio_venta)