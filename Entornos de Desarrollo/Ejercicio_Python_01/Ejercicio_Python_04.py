# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 4: Dados dos números, mostrar la suma, resta, división 
#              y multiplicación de ambos.
# **********************************************************************************
#
import math
print("Deberá de introducir dos números, para mostrar la suma, resta, división y multiplicación de ambos")
numero_1 = int(input("Introduzca el primer número: "))
numero_2 = int(input("Introduca el segundo número: "))

suma = int(numero_1+numero_2)
print("Este es el total de la suma: ", suma)
resta_1 = int(numero_1-numero_2)
print("Este es el total de resta 1: ", resta_1)
resta_2 = int(numero_2-numero_1)
print("Este es el total de resta 2: ",resta_2)
división_1 = float(numero_1/numero_2)
print("Este es el total de división 1: ",división_1)
división_2 = float(numero_2/numero_1)
print( "Este es el total de división 2: ",división_2)
multiplicación = int(numero_1*numero_2)
print( "Este es el total del producto: ",multiplicación)


     