# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 8: Queremos guardar los nombres y la edad de los alumnos de un curso. Realiza 
#              un programa que introduzca el nombre y la edad de cada alumno. El proceso 
#              de lectura de datos terminará cuando se introduzca como nombre un asterisco 
#              (*). Al finalizar se mostrarán los siguientes datos:
# - Todos los alumnos mayores de edad.
# - Los alumnos mayores (los que tienen más edad)
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
# realizamos una lista para los nombres y otra para las edades de cada muchacho

nombreAlumno_Martín=[]
edadAlumno_Martín=[]
seguir = True
# realizamos un bucle con dos variables que depués introduciremos en las listas.
while seguir:
    print("\n")
    nombre=input("Introduce el nombre del alumno: ")
    
    if nombre=="*":
        
        break # sustituimos un seguir = False por no detener el bucle 
    
    edad= int(input("Introduce la edad del alumno: "))
    
    nombreAlumno_Martín.append(nombre)
    edadAlumno_Martín.append(edad)
    
nombres_Martín=[]
for i in range (len(edadAlumno_Martín)):
    
    if edadAlumno_Martín[i]>=18:
        nombres_Martín.append(nombreAlumno_Martín[i])
        
print("Los alumnos mayores de edad son: ",nombres_Martín)
print("\n")  
# vamos a considerar que los más mayores comparten la misma edad osea que son de la misma quinta
mayores=[]
for j in range(len(edadAlumno_Martín)):
    
    if edadAlumno_Martín[j]==max(edadAlumno_Martín):
        mayores.append(nombreAlumno_Martín[j])
    
    
print("Los mayores son: ",mayores)