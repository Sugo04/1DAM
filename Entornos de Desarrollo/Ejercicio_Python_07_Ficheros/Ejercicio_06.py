# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 06: Realice un programa que reciba de nuevo el fichero calificacionfinal.csv 
#               para  generar dos listas, una con los alumnos aprobados y otra con los 
#               alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser
#               mayor o igual que el 75% y la nota final mayor o igual que 5. Se deberá 
#               guardar las dos listas en dos ficheros distintos con los nombres 
#               aprobados.csv y suspensos.csv.
# ****************************************************************************************

# Lee el archivo calificacionfinal.csv
with open('calificacionfinal.csv', 'r', encoding='utf-8') as file_martín:
    lineas_martín = file_martín.readlines()

# eliminamos la primera linea porque son solo los encabezados  ya que  no queremos trabajar con ellos
encabezado_martín = lineas_martín[0]
lineas_martín = lineas_martín[1:]

# creamos las dos listas que luego leeremos para nuestros nuevos ficheros
aprobados_martín = []
suspendidos_martín = []

# realizamos un bucle que recorra las linea en 
for line_martín in lineas_martín:
    # dividimos las lineas en diferentes campos cada uno correspondiente a una columna
    campos_martín = line_martín.strip().split(',')

    # Extrae la asistencia y la nota final
    asistencia_martín = float(campos_martín[2].replace('%', ''))
    nota_final_martín = float(campos_martín[-1])

    # con un condicional comprobamos que el alumno apruebe o suspenda
    if asistencia_martín >= 75 and nota_final_martín >= 5:
        aprobados_martín.append(line_martín)
    else:
        suspendidos_martín.append(line_martín)

# guardamos los parobadoes en el fichero aprobados y a los suspendidos en el de suspendidos
with open('aprobados.csv', 'w', encoding='utf-8') as aprobados_file_martín:
    aprobados_file_martín.write(encabezado_martín)
    aprobados_file_martín.writelines(aprobados_martín)

with open('suspendidos.csv', 'w', encoding='utf-8') as suspendidos_file_martín:
    suspendidos_file_martín.write(encabezado_martín)
    suspendidos_file_martín.writelines(suspendidos_martín)

print("Listas de aprobados y suspendidos generadas correctamente.")
