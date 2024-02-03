# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 13: De una empresa de transporte se quiere guardar el nombre de los conductores 
#              que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# - Nombre: Lista para guardar los nombres de los conductores.
# - kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realiza 
# cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha 
# realizado.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
# vamos a crear una lista denominada días que más tarde nos servirá por su longitud.
#De paso nombramos la otras dos listas necesarias

días_Martín=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
nombres_Martín=[]
totalkms_Martín=[]
# realizamos un bucle que lea los datos que queremos introducir en nuestras dos listas
while True:
    
    print("\n")
    print("---------------------------------------------------------")
    nombre=input("Introduce el nombre del conductor: ")
    
    if nombre=="*":
        
        break
    
    kms_Martín=[]
    for i in range(len(días_Martín)):
        print("-",días_Martín[i],"-")
        km=float(input("Introduce lo que conduciste:"))
        kms_Martín.append(km)
        
    total=sum(kms_Martín)
    print("---------------------------------------------------------")
    
    totalkms_Martín.append(total)
    nombres_Martín.append(nombre)
#realizamos un último bucle que muestre la solución
for j in range(len(nombres_Martín)):
    
    print(nombres_Martín[j]," ha recorrido en total: ",totalkms_Martín[j])
    print("\n")
    