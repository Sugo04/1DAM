# Alumno: Héctor Martín Ortega
#
# ******************************************************************************************
# Ejercicio 04: Codifica un programa en python que nos permita guardar los nombres de los 
#               alumnos de una clase y las notas que han obtenido. Cada alumno puede tener
#               distinta cantidad de notas. Guarda la información en un diccionario cuya 
#               claves serán los nombres de los alumnos y los valores serán listas con las 
#               notas de cada alumno.
#
#               El programa pedirá el número de alumnos que vamos a introducir, pedirá su 
#               nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. 
#               Al final el programa nos mostrará la lista de alumnos y la nota media 
#               obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno
#               que ya existe el programa nos dará un error. 
# ******************************************************************************************
#
# (Solo agregamos el apellido a los diccionarios para mayor legibilidad. Además lo indica el enunciado.)

cantidadAlumnos=int(input("Introduce la cantidad de alumnos que vas a introducir: "))
datosAlumnos_Martín={}
#realizamos un bucle donde introduzcamos las variables (noombres) y lo valores(listas de notas.)
for i in range(cantidadAlumnos):
    
    nombresAlumno=str(input("Introduce el nombre de la fruta: "))
    
    while nombresAlumno in datosAlumnos_Martín:
        print("Error: Este alumno ya existe. Introduce un nombre único.")
        nombresAlumno=str(input("Introduce otro nombre único: "))
    notas=[]
    #realizamos un bucle que no termine a no ser que se introduzca un número negativo. Y que recolecte las notas de cada
    # alumno
    while True:
        nota=float(input(f"Introduce la nora del alumno {nombresAlumno} (<0 para terminar de introducir notas: )"))
        if nota<0:
            break
        else:
            notas.append(nota)
    
    # las listas de notas son el valor de la variable que correponde al nombre del alumno.
    datosAlumnos_Martín[nombresAlumno]=notas
    
#realizamos un bucle que realice la media de cada alumno y nos muetre la solución del ejercicio
#consideremos nombre como la variable y nota como el valor. Y usamos items para mostrar todo.

for nombre,notas in datosAlumnos_Martín.items():
    # la media es la suma de los valores de la lista notas/ la longitud de la misma lista.
    
    media= sum(notas)/len(notas)
    print(f"{nombre} tiene de media un: {media}")