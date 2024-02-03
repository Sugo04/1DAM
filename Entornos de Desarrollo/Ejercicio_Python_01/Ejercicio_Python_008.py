# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO********************************
# Ejercicio 8:  Un vendedor recibe un sueldo base mas un 10% extra por 
#               comisión de sus ventas, el vendedor desea saber cuanto 
#               dinero obtendrá por concepto de comisiones por las tres 
#               ventas que realiza en el mes y el total que recibirá en 
#               el mes tomando en cuenta su sueldo base y comisiones.
# *************************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Deberá de introducir el sueldo base del vendedor, además del monto de cada venta.")

# Pedimos el sueldo y el monto de cada venta

Sueldo_base = float(input("Introduzca el sueldo base aquí: "))

venta_1 = float(input("Introduzca el monto de la venta aquí: "))
venta_2 = float(input("Introduzca el monto de la venta aquí: "))
venta_3 = float(input("Introduzca el monto de la venta aquí: "))

# Realizamos las operaciones convenientes usease hayamos las comisiones y las sumamos
# así como el sueldo total.

comisión_1 = float(venta_1*0.1)
comisión_2 = float(venta_2*0.1)
comisión_3 = float(venta_3*0.1)

total_comisiones = float(comisión_1+comisión_2+comisión_3)

Sueldo_total = float(Sueldo_base+total_comisiones)

# Mostramos en pantalla la solución

print("El sueldo total del vendedor será de : ", Sueldo_total, "euros." )

