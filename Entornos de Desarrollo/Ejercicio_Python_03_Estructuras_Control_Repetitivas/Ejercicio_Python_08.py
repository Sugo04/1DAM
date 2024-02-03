# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 8: Escribe un programa que pida el limite inferior y superior de un intervalo. 
#              Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
#              A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando
#              termine el programa dará las siguientes informaciones:
#
#              La suma de los números que están dentro del intervalo (intervalo abierto).
#              Cuantos números están fuera del intervalo.
#              He informa si hemos introducido algún número igual a los límites del intervalo.
# **********************************************************************************************
#

# Mostramos lo que el usuario debe de hacer con un mensaje en pantalla

print("introduzca dos números")

num1_martín= int(input("primer numero del intervalo: "))
num2_martín= int(input("segundo numero del intervalo: "))

while num2_martín<num1_martín:
    num2_martín= int(input("segundo numero del intervalo(mayor que el primero): "))

num_fuera_intervalo_martín = 0
num_martín= int(input("introduzca números diferentes a 0 (este termina el bucle): ")) 
suma_martín=0
i_martín=0
igual_martín=0
while num_martín!=0:
    num_martín= int(input("introduzca números diferentes a 0 (este termina el bucle): "))
    i_martín=i_martín+1
    suma_martín=suma_martín+num_martín
    if num_martín<num1_martín or num_martín>num2_martín:
        num_fuera_intervalo_martín=num_fuera_intervalo_martín+1
    if num_martín==num1_martín or num_martín==num2_martín:
        igual_martín=igual_martín+1
        
print("la suma de todos lo números son: ", suma_martín)

print("la cantidad de números fuera del intervalo son: ",num_fuera_intervalo_martín)

if igual_martín>0:
    print("se ha introducido algún número igual a los límites del intervalo")