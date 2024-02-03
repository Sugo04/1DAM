# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 11: Escribe un programa que diga si un número introducido por teclado es o no primo.
#               Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
#               Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
#               divisible por algún otro número.
# **********************************************************************************************
#
import math
# Mostramos por un mensaje lo que debe de hacer el usuario

print("Introduce un número para saber si es primo.")

num_martín= int(input("introduce un número (entero): "))
raíz_martín= int(math.sqrt(num_martín))
esPrimo_Martín=True

for i_martín in range(2,raíz_martín+1):
      
      if num_martín%i_martín==0:
           
           esPrimo_Martín=False

if esPrimo_Martín:

    print("Es primo.")

else:
        
    print("NO es primo.")