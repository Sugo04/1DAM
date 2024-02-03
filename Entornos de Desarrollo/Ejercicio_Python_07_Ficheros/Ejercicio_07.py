# Alumno: Héctor Martín Ortega
#
# **********************************************************************************************
# Ejercicio 07: El fichero cotizaciones.csv contiene las cotizaciones de las empresas del
#               IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final 
#               (precio de la acción al cierre de bolsa), Máximo (precio máximo de la
#               acción durante la jornada), Mínimo (precio mínimo de la acción durante 
#               la jornada), Volumen (Volumen al cierre de bolsa), Efectivo 
#               (capitalización al cierre en miles de euros).
#
#               Construir un programa que reciba el fichero de cotizaciones , devuelva un
#               diccionario y lo imprima en la terminal con el mismo formato que el fichero. 
#
#               A continuación se deberá crear una lista de diccionarios con el nombre de 
#               las columnas medibles, su máximo, su mínimo y su media aritmética. Esta 
#               lista se deberá guardar en un fichero llamado ejercicio7_primerapellido en 
#               formato csv.
# ***********************************************************************************************

import csv

# Leemos el archivo csv y iniciamos un diccionario donde meteremos por cada nombre su dinero.
diccionario_cotizaciones_martín = {}
with open('cotizaciones.csv', 'r', encoding='latin-1') as csvfile_martín:
    reader_martín = csv.DictReader(csvfile_martín)
    for row_martín in reader_martín:
        nombre_martín = row_martín['Nombre']
        datos_empresa_martín = {
            'Final': float(row_martín['Final']),
            'Máximo': float(row_martín['Máximo']),
            'Mínimo': float(row_martín['Mínimo']),
            'Volumen': float(row_martín['Volumen']),
            'Efectivo': float(row_martín['Efectivo'])
        }
        diccionario_cotizaciones_martín[nombre_martín] = datos_empresa_martín

# con un bucle mostramos la informacion que tenemos en el diccionario.
for nombre_martín, datos_martín in diccionario_cotizaciones_martín.items():
    print(f"{nombre_martín}: {datos_martín}")

# realizamos las opercaciones que necesitamos para obtener el maximo, minimo, la final, el volumen y el efectivo e iniciamos una lsita que se encargará de
# obtener estos datos
columnas_medibles_martín = ['Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo']
estadisticas_martín = []

for columna_martín in columnas_medibles_martín:
    valores_martín = [datos_m[columna_martín] for datos_m in diccionario_cotizaciones_martín.values()]
    maximo_martín = max(valores_martín)
    minimo_martín = min(valores_martín)
    media_martín = sum(valores_martín) / len(valores_martín)

    estadistica_martín = {
        'Columna': columna_martín,
        'Máximo': maximo_martín,
        'Mínimo': minimo_martín,
        'Media': media_martín
    }

    estadisticas_martín.append(estadistica_martín)

# guardamos todsa las estadísticas que hemos obtenido en un fichero nuevo
with open('ejercicio7_primerapellido.csv', 'w', newline='', encoding='utf-8') as csvfile_martín:
    fieldnames_martín = ['Columna', 'Máximo', 'Mínimo', 'Media']
    writer_martín = csv.DictWriter(csvfile_martín, fieldnames=fieldnames_martín, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer_martín.writeheader()
    for estadistica_m in estadisticas_martín:
        # Convertimos los números a cadena con el punto decimal
        estadistica_str_martín = {key_m: f"{value_m:.2f}" if isinstance(value_m, float) else value_m for key_m, value_m in estadistica_m.items()}
        writer_martín.writerow(estadistica_str_martín)
