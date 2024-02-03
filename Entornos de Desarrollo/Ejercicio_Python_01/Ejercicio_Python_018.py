# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO************************************************
# Ejercicio 18: Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
# *****************************************************************************************
#

# Mostramos un mensaje indicando al usuario lo que debe de hacer

print("Deberá de introducir su nombre y apellidos para obtener sus iniciales.")

# Indicamos con un mensaje donde debe de introducir los datos

nombre = input("Introduzca su nombre: ")

nombres = nombre.split()

if len(nombres)>1:
    apellido_1 = input("Introduzca su primer apellido: ")

    apellido_2 = input("Introduzca su segundo apellido: ")

    # Mostramos la solución.

    print(nombres[0][0],".", nombres[1][0],".",apellido_1[0],".",apellido_2[0],".")

apellido_1 = input("Introduzca su primer apellido: ")

apellido_2 = input("Introduzca su segundo apellido: ")

# Mostramos la solución.

print("Sus iniciales son: ",nombres[0][0],".",apellido_1[0],".",apellido_2[0],".")