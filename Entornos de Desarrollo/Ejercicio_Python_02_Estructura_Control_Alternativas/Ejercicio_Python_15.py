# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO******************************************
# Ejercicio 15: El director de una escuela está organizando un viaje de estudios,
#               y requiere determinar cuánto debe cobrar a cada alumno y cuánto 
#               debe pagar a la compañía de viajes por el servicio. La forma de 
#               cobrar es la siguiente: si son 100 alumnos o más, el costo por cada 
#               alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, 
#               de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta 
#               del autobús es de 4000 euros, sin importar el número de alumnos.
#               Realice un algoritmo que permita determinar el pago a la compañía 
#               de autobuses y lo que debe pagar cada alumno por el viaje.
# ************************************************************************************
#

# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Introduce el número de alumnos para saber cuanto pagará cada uno y cuanto costará el viaje. ")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

alumnos = int(input("Introduce aquí el número de alumnos: "))

if alumnos>=100 :
    dinero= 65
    costo= dinero*alumnos
    
elif alumnos>49 and alumnos<100:
    dinero= 70
    costo= dinero*alumnos
    
elif alumnos<50 and alumnos>29:
    dinero= 95
    costo= dinero*alumnos
    
elif alumnos<30:
    costo=4000
    dinero= "-"

print("El precio del viaje será de ",costo," euros\n",
      "Y cada alumno pagará: ",dinero)