# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 10:  Diseñar el algoritmo correspondiente a un programa que:
# - Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# - Carga la tabla con valores numéricos enteros.
# - Suma todos los elementos de cada fila y todos los elementos de cada columna 
# 	visualizando los resultados en pantalla.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
lista_Martín = []
#realizamos un bucle en el que iniciaremos otro que nos permita leer los número introducidos por el usuario
for i in range(1,6):
	fila = []
	for j in range(1,6):
		fila.append(int(input("Introduce el número de la fila y columna :" )))
	lista_Martín.append(fila)

# Con un bucle realizamos la suma de todos los componentes de la fila
i = 1
for fila in lista_Martín:
	print("La suma de los elemento de la fila es ",sum(fila))
	i += 1

# Hacemos un bucle que sume cada dato dentro de una columna y lo mostramos 
for j in range(1,6):
	suma = 0
	for fila in lista_Martín:
		suma = suma + fila[j - 1]
	print("La suma de los elemento de la columna es " ,suma)
