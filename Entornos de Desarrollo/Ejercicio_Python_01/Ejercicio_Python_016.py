# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 16: Dos vehículos viajan a diferentes velocidades (v1 y v2) y 
# están distanciados por una distancia d. El que está detrás viaja a una 
# velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre
# los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar
# y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro
# **********************************************************************************
#

import math

# Vamos a mostrar un mensaje en pantalla describiendo que debe de hacer el usuario

print("Usted deverá de introducir la distancia entre dos vehículos.\n",
      "Así como las velocidades de ambos automóviles: A(primero),B(segundo). Teniendo "
      ,"en cuenta que la velocidad del segundo auto deberá de ser menor a la del primero")

# Con un mensaje en la pantalla indicaremos dónde debe de introducir los datos el usuario

D = float(input("Introduzca aquí la distancia entre los autos (en Km): "))

V_A = float(input("Introduzca aquí la velocidad del auto A (en Km/h):  "))

V_B = float(input("Introduzca aquí la velocidad del auto B (en Km/h):  "))

while V_B<V_A:
    print ("LA velocidad de B debe deser mayor que la de A")
    V_B = float(input("Introduzca aquí la velocidad del auto B (en Km/h):  "))
# Ahora hayaremos el tiempo, el cual estará en horas y por ende deberémos de pasar
# a minutos.

tiempo = (D/(V_A-V_B))
#lo hacemos entero por comodidad visual de la solución

tiempo_minutos= int(tiempo*60)

# comprobaremos que la solución sea positiva, sino la haremos positiva

if tiempo_minutos < 0:
    tiempo_minutos = -tiempo_minutos
    
# Mostramos con un mensaje en la pantalla la solución

print("El tiempo que le tomará a B de alcanzar a A será de: ",tiempo_minutos," minutos")

