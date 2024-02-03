# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************
# Ejercicio 15: Dadas dos variables numéricas A y B, que el usuario debe 
#               teclear, se pide realizar un algoritmo que intercambie los 
#               valores de ambas variables y muestre cuanto valen al final 
#               las dos variables.
# ****************************************************************************
#

# Mostraremos un mensaje en pantalla en el que se define que se debe hacer

print("Introduzca las variables A y B para que estas tomen el valor de la otra")

# Mostramos un mensaje en pantalla para que el usuario sepa donde debe de 
# introducir los valores numéricos.

A = float(input("Introduzca A: "))
B = float(input("Introduzca B: "))

# Como no podemos asignar primero el valor de uno a otra, haremos una asignacoón
# múltiple. Lo cual nos permitirá modificar ambos valores al mismo tiempo 
# sin ninguna variable extra. Mostraremos la solución con dos mensajes en la pantalla

A, B = B, A

print("Ahora el valor de A es: ", A) 

print("Y el valor de B ahora es: ", B)