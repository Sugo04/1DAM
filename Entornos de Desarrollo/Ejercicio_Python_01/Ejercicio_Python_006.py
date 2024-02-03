# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************
# Ejercicio 6: Calcular la media de tres números pedidos por teclado.
# **********************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Introduzca tres números para realizar su media.")

# Pedimos los tres valores

num_1 = float(input("Introduzca el numero que desee: "))

num_2 = float(input("Introduzca el numero que desee: "))

num_3 = float(input("Introduzca el numero que desee: "))

# Ahora realizamos la cuenta conveniente para dar la solución, y mostramos en
# pantalla la solución.

media = float(num_1+num_2+num_3)
media2 = float(media/3 )
print("La media de los tes números introducidos es: ")