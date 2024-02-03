# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************
# Ejercicio 10: Un alumno desea saber cual será su calificación final en la 
#               materia de Algoritmos. Dicha calificación se compone de los 
#               siguientes porcentajes:
#
#               55% del promedio de sus tres calificaciones parciales.
#               30% de la calificación del examen final.
#               15% de la calificación de un trabajo final.
# ****************************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Introduzca la nota de cada apartado para saber su media.")

# Pedimos los valores necesarios y calculamos el promedio de los parciales
# ya que nuestro código permite al usuario comprobar su promedio sies que no
# lo conoce o no sabe hayarlo.

calif_1 = float(input("Introduzca su primera nota de las"+ 
                      " calificaciones parciales: "))

calif_2 = float(input("Introduzca su primera nota de las"+ 
                      " calificaciones parciales: "))

calif_3 = float(input("Introduzca su primera nota de las"+ 
                      " calificaciones parciales: "))

promedio_parciales= float((calif_1+calif_2+calif_3)/3)

print("El promedio de sus parciales es: ",promedio_parciales)

examen_final = float(input("Introduzca la nota de su examen final: "))

trabajo_final = float(input("Introduzca la nota de su trabajo final: "))

# Realizamos las operaciones convenientes para la resolución del ejercicio

porcentaje_1 = float(promedio_parciales*0.55)
porcentaje_2 = float(examen_final*0.30)
porcentaje_3 = float(trabajo_final*0.15)

calificación_final = float(porcentaje_1+porcentaje_2+porcentaje_3)

# Mostramos en pantalla la solución

print("Su calificación final es un: ",calificación_final)