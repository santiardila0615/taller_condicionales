# programa para solicitar un prestamo 

#input

salario_emp=int(input("Digite su ingreso mensual: "))

deudas=input("¿El empleado tiene deudas? si/no: ")

#proceso 

if salario_emp > 945200:

    if deudas == "no":

        rta = "APROBADO"
        
    else:
        rta = "DENEGADO"
else:

    rta = "DENEGADO"
#output

print("Su prestamo ha sido, " + rta)