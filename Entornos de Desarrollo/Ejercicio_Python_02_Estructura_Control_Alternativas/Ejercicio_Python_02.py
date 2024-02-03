# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 2: Algoritmo que pida un número y diga si es positivo, negativo o 0.
# **********************************************************************************
#

# Mostramos al usuario con un mensaje en pantalla lo que deberá de hacer.

print("Deberá de introducir un número, y el programa el indicará si es: ",
      "negativo, positivo o cero. ")

# Indicamos con mensajes a pantalla, dónde debe de introducir los valores numéricos.

num = float(input("Introduzca número que desee conocer (puede ser decimal): "))

# Realizaremos un switch debido a que son diferentes resultados para una única variable.


if num > 0:
    print("El número introducido es positivo.")
elif num<0:
    print("El número introducido es negativo.")
else:
    print("El número introducido es 0.")
    