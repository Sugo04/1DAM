# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 04: El fichero calificaciones.csv contiene las calificaciones de un curso. 
#               Durante el curso se realizaron dos exámenes parciales de teoría y un 
#               examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de 
#               estos exámenes pudieron repetirlo al final del curso (convocatoria 
#               ordinaria). Realiza un programa que haga lo siguiente: 
#               Reciba el fichero de calificaciones.csv y devuelva una lista de listas, 
#               donde cada lista contiene la información de los exámenes y la asistencia de
#               un alumno. Para ordenar la lista vamos a utilizar una función lambda:
#
#                    ordenados = sorted(csv_reader,key=lambda x:x[0])
#
#               La función sorted recibe como parámetros la lista que deseas ordenar y el 
#               parámetro key es una función que le indica a sorted como debe ordenar, 
#               en este caso lambda x: x[0] le dice a sorted que como todos los elementos 
#               de la lista son listas escoja para comparar el primer valor de cada lista. 
#               Quizás es extraño ver lambda en el código pero es una abreviatura para 
#               funciones, si tienes dudas puede consultar documentaciones oficiales.
#
#               Se deberá mostrar la lista ordenada en pantalla.
# ****************************************************************************************

#importamos csv

import csv

# abrimos el documento csv que queramos y trabajamos con él

with open('calificaciones.csv') as archivo_martín:
    
    csv_reader_martín = csv.reader(archivo_martín)
    
    # nos saltamos la primera fila del documento csv porque se trata de un encabezado
    next(csv_reader_martín)
    
    ordenados_martín = sorted(csv_reader_martín, key=lambda x: x[0])

print()

# Imprimimos nuestra lista de listas que hemos ordenado con lambda
for alumno_martín in ordenados_martín:
    print(alumno_martín, "\n")

    