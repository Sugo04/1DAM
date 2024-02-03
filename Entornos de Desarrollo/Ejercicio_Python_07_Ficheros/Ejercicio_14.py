# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 14: Escribe un programa en python que lea el fichero json libreria.json 
#               con datos de nuestra librería y muestre en la terminal cuántos libros 
#               hay en la librería.
# ****************************************************************************************


import json
# inicializamos un contador para saber cuantos libros hay que nois cuente los libros que haya
contador_libros_martín = 0

#realizamos un bucle abriendo el archivo que cuente los libros que exiten dentro del archivo
#y mostramos la solucion
with open("libreria.json") as archivo_martín:
    datos_libros_martín = json.load(archivo_martín)
    
    for libro_martín in datos_libros_martín['bookstore']['book']:  
        contador_libros_martín += 1
               
print(f"Hay {contador_libros_martín} libros en nuestra librería.")
