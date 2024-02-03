# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 01: Escribe un programa python que pida un número por teclado y que cree un 
#               diccionario cuyas claves sean desde el número 1 hasta el número indicado,
#               y los valores sean los cuadrados de las claves.
# ****************************************************************************************
#
# (Solo agregamos el apellido a los diccionarios para mayor legibilidad. Además lo indica el enunciado.)

import math
# Indicamos al usuario lo que debe de hacer, e iniciamos el diccionario vacío y un contador i en 1.

numeros_Martín={}
i=1
fin=int(input("Introduce hasta que número deseas conocer sus cuadrados: "))
#realizamos un bucle que nos de la solución
for i in range(1,fin+1):
    
    numeros_Martín[i]=math.pow(i,2)
    
for clave,valor in numeros_Martín.items():
    print(clave,"=",valor)