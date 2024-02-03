# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 18: Escriba un programa que permita crear una lista de palabras y que, 
#              a continuación, de tres opciones:
# - Contar: Me pide una cadena, y me dice cuántas veces aparece en la lista
#
# - Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las 
#   apariciones de la primera por la segunda en la lista.
#
# - Eliminar: Me pide una cadena, y la elimina de la lista.
#
# - Mostrar: Muestra la lista de cadenas
#
# - Terminar
#.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.)
#realizamos la lista de palabras que necesitamos realizar.
listaPalabras_Martín=[]
print("\n")
cadena=input("Introduce la cadena que desees guardar en la lista. (Introduce SPACE para salir): ")
listaPalabras_Martín.append(cadena)
while cadena!=" ":
    print("\n")
    cadena=input("Introduce la cadena que desees guardar en la lista. (Introduce SPACE para salir): ")
    listaPalabras_Martín.append(cadena)

listaPalabras_Martín.pop()
print("\n")
print("Ahora vamos a ver qué desea hacer con la lista: ")
print("1. Contar")
print("2. Modificar")
print("3. Eliminar")
print("4. Mostrar")
print("5. Salir")
salida=int(input("Introduce lo que desees hacer con la lista: "))
print("\n")

while salida!=5:
    
    if salida==1:
        palabra=input("Introduce la cadena que desees conocer cuántas veces aparece: ")
        # usamos el .count
        print("La cantidad de veces que se repite la palabra '",palabra,"' es ",listaPalabras_Martín.count(palabra))
        print("\n")
        
        salida=int(input("Introduce lo que desees hacer con la lista: "))
        print("\n")
        
    elif salida==2:
        palabra=input("Introduce la palabra de la lista que desees buscar: ")
        palabra2=input("Introduce la palabra de la lista que desees modificar: ")
        indice = 0
        for i in range(len(listaPalabras_Martín)):
            if listaPalabras_Martín[i] == palabra:
                listaPalabras_Martín[i] = palabra2

        salida=int(input("Introduce lo que desees hacer con la lista: "))   
        print("\n")

    elif salida == 3:
        palabra=input("Introduce tu cadena: ")
        
        if palabra in listaPalabras_Martín:
            print("El elemento que vamos a eliminar es ",palabra,".")
            while palabra in listaPalabras_Martín:
                
                listaPalabras_Martín.remove(palabra)
            
        print("\n")
        salida=int(input("Introduce lo que desees hacer con la lista: "))   
        print("\n")

    elif salida == 4:
        for i in range(len(listaPalabras_Martín)): 
            print(listaPalabras_Martín[i]," ",end="")
        print("\n")
        salida=int(input("Introduce lo que desees hacer con la lista: "))   
        print("\n")
        
    elif salida == 5:
        print("\n")
        print("Adiós.")

    else:
        print("Valor no válido, introdúzcalo de nuevo.")
        salida=int(input("Introduce lo que desees hacer con la lista: "))
