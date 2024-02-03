# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 11: Diseñar el algoritmo correspondiente a un programa que:
# - Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# - Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz 
#   tomen el valor 1
#   y el resto el valor 0.
# - Muestra el contenido de la tabla en pantalla.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
#realizamos una matriz por lo que haremos una lista

lista_Martín=[]
for i in range(5):
    # realizamos una lista de las filas donde guardemos los valores necesarios 
    
    fila_Martín=[]
    #colocamos uno en las diagonales (lo cual me recuerda al cálculo del deterinante de una matriz.)
    for j in range(5):
        if i==j or i==4-j:
            fila_Martín.append(1)
        else:
            fila_Martín.append(0)
    
    lista_Martín.append(fila_Martín)
    
# mostarmos la matriz con un bucle que imprima la solución.

for fila_Martín in lista_Martín:
    for k in fila_Martín:
        print(k," ",end="")
    #colocamos un salto de línea entre filas
    print()
  
  
	
