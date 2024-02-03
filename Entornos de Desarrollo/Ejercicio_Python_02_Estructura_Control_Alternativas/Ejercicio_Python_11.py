# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 11: Programa que lea 3 datos de entrada A, B y C. Estos corresponden
#               a las dimensiones de los lados de un triángulo. El programa debe 
#               determinar que tipo de triangulo es, teniendo en cuenta los 
#               siguiente:
#
#               Si se cumple Pitágoras entonces es triángulo rectángulo
#               Si sólo dos lados del triángulo son iguales entonces es isósceles.
#               Si los 3 lados son iguales entonces es equilátero.
#               Si no se cumple ninguna de las condiciones anteriores, es escaleno.
# **********************************************************************************
#
import math
# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Deberá introducir tres lados de un triángulo para saber cómo es.")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

A = float(input("Introduce aquí el lado A: "))

B = float(input("Introduce aquí el lado B: "))

C = float(input("Introduce aquí el lado C: "))

if A == math.sqrt(math.pow(B,2)+math.pow(C,2)):
    print("Es un triángulo rectángulo.")
elif A == B or B == C or C == A:
    print("Es un triángilo isósceles.")
elif A == B and B == C:
    print("Es un triángulo equilátero.")
else:
    print("Es escaleno.")


