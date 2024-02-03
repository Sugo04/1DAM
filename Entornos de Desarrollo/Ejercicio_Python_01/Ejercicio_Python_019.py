# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 19: Escribir un algoritmo para calcular la nota final de un estudiante, 
# considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y 
# por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
# **********************************************************************************
#

# Mostramos un mensaje explicando al usuario que debe de hacer

print("Introduzca la cantidad de respuestas correctas, incorrectas y en blanco ",
      "que hayas tenido en el examen.")

# Indicamos con un mensaje donde debe introducir cada dato y sacamos las preguntas
# totales del examen.

correctas = int(input("Introduzca la cantidad de respuestas correctas: "))

incorrectas = int(input("Introduzca la cantidad de respuestas incorrectas: "))

resp_blanco = int(input("Introduzca la cantidad de respuestas en blanco: "))

total_preguntas = int(correctas+incorrectas+resp_blanco)

# Realizamos las operaciones pertinentes y mostramos la solución en pantalla

nota_total = float((correctas*5)+(incorrectas*(-1)))

print("El resultado obtenido por el estudiante en ",total_preguntas," preguntas es de: ",nota_total)

print("Su nota sobre 10 sería: ",float((nota_total/(total_preguntas*5))*10))


