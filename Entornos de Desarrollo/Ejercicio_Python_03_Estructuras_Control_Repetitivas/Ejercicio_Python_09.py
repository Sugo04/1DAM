# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 9: Escribe un programa que dados dos números, uno real (base) y un entero positivo 
#              (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar
#              el operador de potencia.
# **********************************************************************************************
#

#mostramos al usuario lo que debe de hacer.

print("introduzca un número como Base y otro como exponente.")

base=int(input("Introduzca aquí la base: "))

exponente=int(input("Introduzca aquí el exponente: "))

# Comprobamso que no nos pongan un exponente negativo.

while exponente<0:
    
    exponente=int(input("Introduzca aquí el exponente(no negativo): "))
    
# Realizamos el bucle que no dará la slución e inicializamos un contador llamado potencia en 1
potencia=1
while exponente>=1:
    
    exponente=exponente-1
    potencia=potencia*base

print("La potencia es igual a: ",potencia)


