# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 13: Escribe un programa en python que lea el fichero *movies.json con datos 
#               de películas. A continuación deberá crear un fichero 
#               primerapellido_peliculasaventuras.json con los títulos de las películas 
#               cuyo género incluya aventura.
# ****************************************************************************************

import json
# creamos un diccionario y una lista que guarden las peliculas
peliculas_martín = {}
peliculas_aventuras_martín = []

# abrimos el fichero y guardaamos en el diccionario las listas y en las listas las peliculas de aventura
with open("movies.json") as archivo_martín:
    datos_peliculas_martín = json.load(archivo_martín)
    
    for datos_martín in datos_peliculas_martín:
        if "Adventure" in datos_martín['genres']:
            peliculas_aventuras_martín.append(datos_martín['title'])
    
    peliculas_martín = peliculas_aventuras_martín

# guardamos las peliculas de aventuras en un fichero json nuevo
with open("martín_peliculasaventuras.json", 'w') as archivo_nuevo_martín:
    json.dump(peliculas_aventuras_martín, archivo_nuevo_martín, indent=1)
