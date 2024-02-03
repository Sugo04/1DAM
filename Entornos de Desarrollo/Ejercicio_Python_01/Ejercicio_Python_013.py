# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************
# Ejercicio 13: Realizar un algoritmos que lea un número y que muestre 
#               su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna 
#               función predefinida que permita calcular la raíz cúbica, 
#               ¿Cómo se puede calcular?
# ****************************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Introduzca el número del que desee saber la raíz cuadrada" 
      , "y la raíz cúbica.")

# Mostramos en pantalla el lugar donde debe de introducir el valor

num = float(input("Introduzca aquí el valor que desee: "))

# Para realizar la raíz cúbica voy a elevar el valor a un tercio, 
# he investigado y hay una función de math que permite realizarlo sin embargo,
# considero esto algo más práctico y visual.

cuadrada = float(math.sqrt(num))

cúbica = float(pow(num,(1/3)))

# Mostraremos con un par de  mensajes en pantalla las soluciones.

print("La raíz cuadrada de ", num, " es ", cuadrada)

print("La raíz cúbica de ", num, " es ", cúbica)

