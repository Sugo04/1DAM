# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 3: Se quiere realizar un programa que lea por teclado las 5 notas obtenidas
#              por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar
#              todas las notas, la nota media, la nota más alta que ha sacado y la menor.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.)
# -  buscamos que solo lea 5 valores, por eso el for _ in range (5)  -

print("\n")
print("*********************************************************************************************")
lista_Martín =[int(input("Introduce el número aquí: ")) for _ in range(5)]
print("\n")

print("****************************************************************************")
print( "Su lista de valores son: ",lista_Martín)
print("****************************************************************************")

print("\n")

# nos acercioramos de que las notas sean entre 0 y 10
i=0
while lista_Martín[i]<0 or lista_Martín[i]>10:

    lista_Martín =[int(input("Introduce el número aquí: ")) for _ in range(5)]
    print("\n")

    i=i+1



# Realizamos un bucle para la nota media , y buscar la más alta y la menor.

j=0
suma=0

máximo_Martín=0
mínimo_Martín=10

while i<len(lista_Martín):
    
    suma=suma+lista_Martín[i]

    if lista_Martín[i]>máximo_Martín:

        máximo_Martín=lista_Martín[i]

    if lista_Martín[i]<mínimo_Martín:

        mínimo_Martín=lista_Martín[i]
    
    i=i+1

print("La media de tus notas es: ",suma/len(lista_Martín))
print("Tu nota máxima es: ",máximo_Martín)
print("Tu nota mínima es: ",mínimo_Martín)
print("\n")

print("*********************************************************************************************")