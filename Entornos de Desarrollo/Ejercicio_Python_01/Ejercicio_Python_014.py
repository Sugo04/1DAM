# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************
# Ejercicio 14: Dado un número de dos cifras, diseñe un algoritmo que 
#               permita obtener el número invertido. Ejemplo, si se introduce 
#               23 que muestre 32.
# ****************************************************************************
#

# Mostramos con un mensaje en pantalla, lo que se busca lograr.

from pydoc import stripid


print("Deberá de introducir un valor de dos dígito que se le devolverá" 
      ,"el 'inverso', por ejemplo si da 23 le devolverá 32.")

# Indicaremos con un mensaje que se mostrará en pantalla dónde debe de 
# introducir el usuario el valor.

num = int(input("Introduzca el valor numérico(entero y de dos dígitos) aquí: "))

# Lo que haremos será crear dos variables: decenas y unidades
# Los cuales obligaremos al programa a leerlos al revés en el mensaje que mostraremos
# en pantalla para dar la solución

decenas = int(num/10)
unidades = int(num%10)
# Calculamos el número invertido de esta manera.

invertido = int((unidades*10+decenas))

print("El inverso de ",num," sería ",invertido)
