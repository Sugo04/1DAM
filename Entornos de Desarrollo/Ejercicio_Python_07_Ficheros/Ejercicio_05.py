# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 05: Realice un programa que reciba de nuevo el fichero calificaciones.csv 
#               para añadir a cada lista de cada alumno un nuevo elemento, será la Nota 
#               Final del curso. El peso de cada parcial de teoría en la nota final es de 
#               un 30% mientras que el peso del examen de prácticas es de un 40%. Si el 
#               alumno ha realizado alguna recuperación ordinaria, para el cálculo de la 
#               nota final se tomará esta como última nota del alumno. Se deberá mostrar 
#               finalmente en la terminal la lista ordenada y será guardada en un fichero 
#               que se llamará calificacionfinal.csv.
# ****************************************************************************************

import csv

# Lee el archivo original
with open('calificaciones.csv', 'r', encoding='latin-1', newline='') as archivo_martín:
    datos_martín = csv.DictReader(archivo_martín)
    filas_martín = list(datos_martín)

for alumno_martín in filas_martín:
    
    # comprobamos las notas del primer ordinario y parcial, en caso de no existir ponemos que son 0.
    if alumno_martín['Ordinario1']:
        parcial1_martín = float(alumno_martín['Ordinario1'])
    elif alumno_martín['Parcial1']:
        parcial1_martín = float(alumno_martín['Parcial1'])
    else:
        parcial1_martín = 0
        
    # hacemos lo mismo con el 2 y las prácticas
    if alumno_martín['Ordinario2']:
        parcial2_martín = float(alumno_martín['Ordinario2'])
    elif alumno_martín['Parcial2']:
        parcial2_martín = float(alumno_martín['Parcial2'])
    else:
        parcial2_martín = 0
        
    if alumno_martín['OrdinarioPracticas']:
        parcial3_martín = float(alumno_martín['OrdinarioPracticas'])
    elif alumno_martín['Practicas']:
        parcial3_martín = float(alumno_martín['Practicas'])
    else:
        parcial3_martín = 0
        
    # creamos la nota final.
    alumno_martín['NotaFinal'] = round(parcial1_martín * 0.3 + parcial2_martín * 0.3 + parcial3_martín * 0.4, 2)
    
# ordenamos con .sort() y una función lambda para que sea de mayor a menor
filas_martín.sort(key=lambda x: x['NotaFinal'], reverse=True)

print("Las notas finales son: ")

for i_martín in filas_martín:
    print(f"{i_martín['Apellidos']},{i_martín['Nombre']} --> {i_martín['NotaFinal']}\n")
    
# guardamos estos datos en la lista nueva y la añadimos al nuevo archivo csv
with open('calificacionfinal.csv', mode='w', encoding='utf-8', newline='') as archivo_martín:
    escribir_martín = csv.writer(archivo_martín)
    escribir_martín.writerow(datos_martín.fieldnames + ['NotaFinal'])
    
    for alumno_martín in filas_martín:
        escribir_martín.writerow([alumno_martín[field] for field in datos_martín.fieldnames + ['NotaFinal']])
