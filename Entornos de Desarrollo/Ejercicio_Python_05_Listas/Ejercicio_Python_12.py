# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 12: Diseñar el algoritmo correspondiente a un programa que:
# - Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# - Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones 
#   o elementos que delimitan la tabla,
#   es decir, las más externas, mientras que el resto de los elementos contendrán el valor 
#   0.
# - Visualiza el contenido de la matriz en pantalla.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
# realizamos una lista denominada tabla y la metemos en un bucle 

tabla_Martín=[]
for i in range(5):
    #agregamos una lista fila, que recoja el valor de cada uno de los valores de esa fila
    fila_Martín=[]
    #realizamos otro bucle para las columnas (15)
    for j in range(15):
        if i==0 or i==4 or j==0 or j==14:
            fila_Martín.append(1)
        else:
            fila_Martín.append(0)
    tabla_Martín.append(fila_Martín)
            
#con el bucle que recoge los valores terminado, mostramos la matriz, por supuesto que con otro bucle
for fila_Martín in tabla_Martín:
    for k in fila_Martín:
        print(k," ",end="")
    #colocamos un salto de línea entre filas
    print()

