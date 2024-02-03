# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 1: Algoritmo que pida dos números e indique si el primero es mayor 
#              que el segundo o no.
# **********************************************************************************
#

# Mostramos al usuario con un mensaje en pantalla lo que deberá de hacer.

print("Deberá de introducir dos números distintos, y se le devolverá el primero ",
      "siempre y cuando sea mayor que el segundo. ")

# Indicamos con mensajes a pantalla, dónde debe de introducir los valores numéricos.

num_1 = float(input("Introduzca el primer número (puede ser decimal): "))

num_2 = float(input("Introduzca el segundo número (puuede ser decimal): "))

# Realizamos el condicional conveniente para dar la solución con un mensaje a la pantalla

if num_1>num_2:

    print(num_1, " es mayor que ", num_2)
else: 

    print(num_1, " no es mayor que ", num_2)
    