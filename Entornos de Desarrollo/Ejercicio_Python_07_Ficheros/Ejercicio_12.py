# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 12: Escribe un programa en python que lea el fichero *movies.json con datos 
#               de películas. A continuación deberá crear un fichero 
#               primerapellido_pelicula1994.json con los títulos de las películas  
#               que se hayan estrenado en 1994.
# ****************************************************************************************

import json
# creamos un diccionario y una lista que guarden las peliculas
peliculas_martín = {}
peliculas_1994_martín = []
# relizamos un bucle que compruebe que las peliculas sean de 1994 con el valor de su año.
with open("movies.json") as archivo_martín:
    datos_peliculas_martín = json.load(archivo_martín)
    
    for datos_martín in datos_peliculas_martín:
        if datos_martín['year'] == '1994':
            peliculas_1994_martín.append(datos_martín['title'])
    
    peliculas_martín = peliculas_1994_martín
# guardamos las peliculas en un nuevo archivo json
with open("martín_peliculas1994.json", 'w') as archivo_nuevo_martín:
    json.dump(peliculas_1994_martín, archivo_nuevo_martín, indent=1)
