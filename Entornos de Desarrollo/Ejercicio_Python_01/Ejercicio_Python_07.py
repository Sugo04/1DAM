# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO********************************
# Ejercicio 7: Realiza un programa que reciba una cantidad de minutos y 
#              muestre por pantalla a cuantas horas y minutos corresponde.
#              Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
# *************************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Deberá de introducir una cantidad cualquiera de minutos.")

# Pedimos los minutos

minutos_pedidos = int(input("Introduzca los minutos aquí: "))

# Realizamos las operaciones convenientes

horas= int(minutos_pedidos/60)  

minutos= int(minutos_pedidos%60)

#  mostramos en pantalla la solución

print("Lo que hs introducido es el equivalente a: " , horas , " horas y " ,minutos
      , " minutos")