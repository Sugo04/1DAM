# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************************
# Ejercicio 20: Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de 
#               números primos que queremos mostrar.
# *******************************************************************************************************
#

import math
# Mostramos por un mensaje lo que debe de hacer el usuario

print("Introduce un número para esa cantidad de primos.")
print("\n")

cantidadPrimos_Martín=int(input("Introduce aquí la cantidad: "))
print("\n")

print("Los ",cantidadPrimos_Martín,"números primos, son: ")

# inicializamos dos contadores, uno de ellos en 2. 

i_Martín=0

num2_Martín=2

# realizamos el primer bucle, este alcanzará el número que hemos introducido.

while i_Martín<cantidadPrimos_Martín:
    
    esPrimo_Martín=True
    #agregamos otro contador 
    j_Martín=2
    
    while j_Martín<=math.sqrt(num2_Martín) and esPrimo_Martín:
        #comprobamos si son primos
        if num2_Martín%j_Martín==0:
            esPrimo_Martín=False
        j_Martín=j_Martín+1
            
    #agregamos el último contador para que el programa detecte que pasamos de número
    if esPrimo_Martín:
        i_Martín=i_Martín+1
        print(num2_Martín)
    num2_Martín=num2_Martín+1

            
    

