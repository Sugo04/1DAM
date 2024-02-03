# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*************************************
# Ejercicio 12: Escribir un programa que lea un año indicar si es bisiesto. 
#               Nota: un año es bisiesto si es un número divisible por 4, pero 
#               no si es divisible por 100, excepto que también sea divisible 
#               por 400
# ******************************************************************************
#

# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Deberá introducir el año que desee para saber si es bisiesto.")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

Año = int(input("Introduce aquí el año: "))

if Año%4 == 0 and Año%100 != 0  or Año%400 == 0:
    print ("Es bisiesto")
else :
    print("No es bisiesto")
  