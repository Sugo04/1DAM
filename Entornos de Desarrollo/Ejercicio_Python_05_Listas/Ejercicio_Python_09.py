# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 9: Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un 
#               programa que de la siguiente información:
# - La temperatura media de cada día
# - Los días con menos temperatura
# - Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima 
#   coincide con ella.
#   Si no existe ningún día se muestra un mensaje de información.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
# tomamos una lista bidimensional. El primer puesto será la temperatura máxima, y el segundo la mínima.
# Y realizamos un bucle que lea los datos de las teperatuas y las guarde.

día_Martín=[]

# vamos a realizar una lista que recoja las temperaturas medias del día.
tempMedia_Martín=[]
for i in range(5):
    
    tempMin= int(input("Introudce la temperatura mínima del día: "))
    tempMáx= int(input("Introduce la temperatura máxima del día: "))
    print("\n")
    media=(tempMin+tempMáx)/2
    día_Martín.append([tempMáx,tempMin])
    tempMedia_Martín.append(media)
    
# mostramos la temperatura media de cada día
print(tempMedia_Martín)
print("\n")    

# mostramos el día con menor temperatura ¿media?
        
print("La temperatura mínima media será: ",min(tempMedia_Martín))

valor=int(input("introduzca un valor cualquiera: "))
días_Martín=[]
for i in range(len(día_Martín)):
    
    if valor in día_Martín[i]:
        
        día2=día_Martín[i]
        días_Martín.append(día2)
    
if len(días_Martín)==0:
    
    print("No hay ningun dia con esa temperatura máxima.")
else:
    
    print(días_Martín)