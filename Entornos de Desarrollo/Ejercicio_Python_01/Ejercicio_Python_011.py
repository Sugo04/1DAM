# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************
# Ejercicio 11:  Pide al usuario dos números y muestra la “distancia” entre 
#                ellos (el valor absoluto de su diferencia, de modo que el 
#                resultado sea siempre positivo).
# ****************************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Deberás de introducir dos valores numéros diferente ",
      " para mostrar la distancia entre ellos (valor absoluto)")

# Introduciremos ambos números con un mensaje que se mostrará en pantalla 
# indicando donde deben introducirse.

num_1 = float(input("Introduzca el primer valor: "))

num_2 = float(input("Introduzca el segundo valor: "))

# Podríamos resolver el ejercicio con un condicional, haciendo que cuando
# la resta de sendo números sea negativo, el resto deba de multiplicarse por 
# (-1), sin embargo usaremos una de las aplicaciones de python,abs.
# Mostraremos la solución con un mensaje en la pantalla

print("La distancia entre ",num_1," y ",num_2,"es: ",abs(num_1-num_2))
