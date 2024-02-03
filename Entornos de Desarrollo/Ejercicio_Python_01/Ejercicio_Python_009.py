# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************
# Ejercicio 9: Una tienda ofrece un descuento del 15% sobre el total de la
#              compra y un cliente desea saber cuanto deberá pagar finalmente 
#              por su compra.
# ****************************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Deberá de introducir el valor total de su compra.")

# Pedimos el valor de la compra a la persona

total_compra = float(input("Introduzca el valor aquí: "))


# Realizamos las operaciones adecuadas

descuento = float(total_compra-(total_compra*0.15))

# mostramos la solución en pantalla

print("El valor de la compra tras aplicar el descuento es de: ", descuento, 
      "euros")
