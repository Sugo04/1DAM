# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************
# Ejercicio 7: Realiza un algoritmo que calcule la potencia, para ello 
#              pide por teclado la base y el exponente. Pueden ocurrir 
#              tres cosas:
#              El exponente sea positivo, sólo tienes que imprimir 
#              la potencia.
#              El exponente sea 0, el resultado es 1.
#              El exponente sea negativo, el resultado es 1/potencia 
#              con el exponente positivo.
# **********************************************************************
#
import math
# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Introduzca la base y el exponente de la operación (a^b).")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

num_1 = int(input("Introduce aquí la base de la operación: "))

num_2 = int(input("Introduce aquí el exponente de la operación: "))

# realizamos el condicional conveniente y mostramos el resultado en pantalla
if num_2<0 :
   print("El resultado de elevar ",num_1," a ",num_2," es: ",float((1/math.pow(num_1, (num_2)*(-1)))))
elif num_2 == 0:
    print("El resultado de elevar ",num_1," a ", num_2," es: 1")
else :
    print("El resultado de elevar ",num_1," a ",num_2," es: ",float(math.pow(num_1, num_2)))
