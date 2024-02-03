# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 3: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# **********************************************************************************
#

print ("Deberá de introducir los catetos(b y c) de un triángulo para encontrar ",
       "la hipotenusa (a)")

cateto_b =  int(input("Introduzca el cateto b: "))

cateto_c =  int(input("Introduzca el cateto c: "))

import math

hipotenusa_a = math.sqrt(pow(cateto_b,2)  + pow(cateto_c,2) )

print("La hipotenusa (a) del triángulo de los catetos que has introducido es: ",
       hipotenusa_a)