# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*************************************
# Ejercicio 10: Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios
#               r1,r2 de dos circunferencias y las clasifique en uno de estos 
#               estados:
#
#               - exteriores
#               - tangentes exteriores
#               - secantes
#               - tangentes interiores
#               - interiores
#               - concéntricas
# ******************************************************************************
#
import math
# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Deberá introducir las coordenadas de dos circulos así como sus radios para ver su posición.")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

X_1 = float(input("Introduce aquí X1: "))

Y_1 = float(input("Introduce aquí Y1: "))

Radio_1 = float(input("Introduce aquí Radio1: "))

X_2 = float(input("Introduce aquí X2: "))

Y_2 = float(input("Introduce aquí Y2: "))

Radio_2 = float(input("Introduce aquí Radio1: "))

#Realizamos la distancia entre centros de circunferencias la cual necesitamos para 
# conocer sus posiciones de una respecto a la otra

distancia_centros = math.sqrt(math.pow(X_2-X_1,2)+math.pow(Y_2-Y_1,2))

# Realizamos un switch y agregamos en el mensaje a pantalla la solución.
# Dos circunferencias pueden ser consideradas matemáticamente concéntricas si es que 
# no se haya su posición, y tmb cuando distancia_centros = 0 y r1 = r2. 

if distancia_centros > Radio_1+Radio_2:
    print("Son exteriores")
elif distancia_centros==Radio_1+Radio_2:
    print("Son tangentes exteriores")
elif distancia_centros<(Radio_1+Radio_2) and distancia_centros> abs(Radio_1-Radio_2):
    print("Son secantes")
    # Usamos abs(valor absoluto)
elif distancia_centros==abs(Radio_1-Radio_2):
    print("Son tangentes interiores")
elif distancia_centros<abs(Radio_1-Radio_2):
    if distancia_centros== 0:
        print("Son concéntricas")
    else:
        print("Son interiores")
        
# Fin programa, Recuerde, secantes son dos puntos de corte entre las circunferencias