# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 15: Escribe un programa en python que lea el fichero json libreria.json con 
#               datos de nuestra librería, recibe por teclado un límite inferior y 
#               superior para el precio y muestre en la terminal todos los libros cuyo 
#               precio esta en ese intervalo.
# ****************************************************************************************

import json
#pedimos el inervalo economico de los libros que deseamos
precio_min_martín = float(input("Introduce el precio mínimo que buscas en un libro: "))
precio_max_martín = float(input("Introduce el precio máximo que buscas en un libro: "))
libros_asequibles_martín = []

print("\n")
#abrimos el json y buscamos los libros que cumplan el intervalo y los mostramos
with open("libreria.json") as archivo_martín:
    datos_libros_martín = json.load(archivo_martín)
    
    for libro_martín in datos_libros_martín['bookstore']['book']:
        if precio_min_martín <= float(libro_martín['price']) <= precio_max_martín:
            libros_asequibles_martín.append(libro_martín['title']['__text'])

if not libros_asequibles_martín:
    print(f"No hay libros entre {precio_min_martín}-{precio_max_martín}")
else:
    for titulo_libro in libros_asequibles_martín:
        print(titulo_libro)

            