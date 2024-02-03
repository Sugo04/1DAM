# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 17: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS 
# segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
# **********************************************************************************
#

# Mostramos en pantalla un mensaje dando instrucciones al usuario

print(" Deberá de introducir la hora, minutos y segundos a los cuales salió de "
      ,"la ciudad A, dirección a la ciudad B. También introduzca el tiempo que",
      " tarda en llegar en segundos por favor.")

# Mostramos donde debe de introducir los valores con un mensaje a la pantalla

HH= int(input("Introduzca la hora: "))

MM= int(input("Introduzca los minutos: "))

SS= int(input("Introduzca los segundos: "))

T= int(input("Introduzca el tiempo que tarda en llegar en segundos: "))

# Realizaremos las operaciones convenientes antes de dar el resultado en un mensaje 
# a la pantalla. Entre las operaciones, deberemos de pasar la hora inicial a segundos

tiempo = int((HH*3600)+(MM*60)+SS)

tiempo_total= int(tiempo+T)

# ahora deberemos de sacar la hora de llegada, haciendo la operación inversa de tiempo

HH = int(tiempo_total/3600)
if HH>23:
    HH = (00+(HH-23))
tiempo_restante= tiempo_total%3600
MM = int(tiempo_restante/60)
SS = tiempo_restante%60

print("La hora de llegada con un tiempo de tardanza de ",T," segundos, es a las ",
      HH,":",MM,":",SS)
 


