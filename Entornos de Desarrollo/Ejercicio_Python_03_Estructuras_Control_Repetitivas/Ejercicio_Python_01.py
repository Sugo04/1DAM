# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO********************************************
# Ejercicio 1: Crea una aplicación que pida un número y calcule su factorial 
#              (El factorial de un número es el producto de todos los enteros entre 
#              1 y el propio número y se representa por el número seguido de un signo
#              de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)
# **************************************************************************************
#

# Mostramos con un mensaje en pantalla lo que el usuario deberá de hacer.

print("Deberá introducir un número entero del que desee saber su factorial.")

# Mostramos con un mensaje en pantalla dónde debe insertar el valor de la variable.

num_Martín = int(input("Introduzca aquí el valor del número que desee conocer su factorial: "))

# Declaramos un contador para realizar el bucle pertinente.

i_Martín = 1

while num_Martín>1:

    i_Martín=i_Martín*num_Martín
    
    num_Martín= num_Martín-1

# Mostramos con un mensaje en la pantalla la solución.

print("El factorial del número deseado es: ",i_Martín)