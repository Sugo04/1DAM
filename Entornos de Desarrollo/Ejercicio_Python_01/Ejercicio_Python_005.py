# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************
# Ejercicio 5: Escribir un programa que convierta un valor dado en 
#              grados Fahrenheit a grados Celsius. Recordar que la 
#              fórmula  para la conversión es:
#
# C = (F-32)*5/9
# **********************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje que indica que debe de introducir el dato.

print("Deberá de introducir una cantidad de grados Farenheit para pasarlo a "+
      "Celsius.")
F = float(input("Introduzca la cantidad que desee (en Farenheit): "))

# Introducimos el valor de los grados celsius y mostramos 
# la solución en pantalla

C = float(F-32)*(5/9) 
print("Los ",F," Farenheit que has introducido son: ",C," º")


