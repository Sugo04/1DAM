# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************
# Ejercicio 12: Pide al usuario dos pares de números x1,y2 y x2,y2, que 
#               representen dos puntos en el plano. Calcula y muestra la 
#               distancia entre ellos.
# ****************************************************************************
#

# Importamos el fichero "math".
import math

# Mostramos en pantalla el mensaje de lo que deberá de hacer el usuario.

print("Introduzca los puntos x e y de cada punto.")

# Pedimos los valores necesarios mostrando un mensaje en pantalla que los 
# acompañe para identificarlos

X = float(input("Introduzca X del primer punto: "))

Y = float(input("Introduzca Y del primer punto: "))

X2 = float(input("Introduzca X2 del segundo punto: "))

Y2= float(input("Introduzca Y2 del segundo punto: "))

# Operamos el cuadrado de la suma de los componentes x e y antes de operar
# con la solución.

valor_1= float(pow((X+Y),2))

valor_2= float(pow((X2+Y2),2))

# Ahora si resolveremos el ejercicio, desarrollando la cuenta de la solución
# y mostrándola e pantalla

distancia = float(math.sqrt(valor_1+valor_2))
print("La distancia entre los puntos", (X,Y), " y ", (X2,Y2), "es :" , distancia)
