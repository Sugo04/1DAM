# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 3: Escribe un programa que lea un número e indique si es par o impar.
# **********************************************************************************
#

# Mostramos al usuario con un mensaje en pantalla lo que deberá de hacer.

print("Deberá de introducir un número, y el programa el indicará si es: ",
      "par o impar. ")

# Indicamos con mensajes a pantalla, dónde debe de introducir los valores numéricos.

num_1 = float(input("Introduzca número que desee conocer (puede ser decimal): "))

# Realizaremos el condicional conveniente y mostramos la solución en pantalla

if (num_1%2) == 0:

    print("El número introducido es par")
else:
    print("El número introducido es impar")
    