# Alumno: Héctor Martín Ortega
#
# **************************************************************************************
# Ejercicio 1: Realizar un programa que inicialice una lista con 10 valores aleatorios
#              (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la 
#              lista junto con su cuadrado y su cubo.
# **************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.)

# -Importamos la libreria random debido a que necesitremos usar un random. Y la libreria math para los exponentes-
import random

import math

# - Colocamos el random.randint entre 1 y 10 para que solo genere valores entre 1 y 10; 
#  y buscamos que solo genere 10 valores, por eso el for _ in range (10)  -

print("\n")
print("*********************************************************************************************")
lista_Martín =[random.randint(1,10) for _ in range(10)]

print( "Su lista de valores son: ",lista_Martín)
print("\n")

# - Inicializamos un contador que nos apoyará al realizar el bucle que haga los 
#   los cubos y cuadrados de cada elemento de la lista. Y muestre la solución.-

i=0

while i<10:

    print("****************************************************************************")
    print("El cubo y cuadrado de ",lista_Martín[i]," son: ", math.pow(lista_Martín[i],2)," y ", math.pow(lista_Martín[i],3))
    print("****************************************************************************")
    print("\n")
    
    i=i+1

print("*********************************************************************************************")
