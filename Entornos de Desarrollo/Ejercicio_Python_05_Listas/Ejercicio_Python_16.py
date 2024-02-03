# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 16: Vamos a crear un programa que tenga el siguiente menú:
# - Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# - Añadir número de la lista en una posición: Me pide un número y una posición, y si la 
#   posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# - Longitud de la lista: Te muestra el número de elementos de la lista.
# - Eliminar el último número: Muestra el último número de la lista y lo borra.
# - Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra 
#   de ella (la posición se pide a partir de 1).
# - Contar números: Te pide un número y te dice cuántas apariciones hay en la lista.
# - Posiciones de un número: Te pide un número y te dice en qué posiciones está (contando
#   desde 1).
# - Mostrar números: Muestra los números de la lista
# - Salir
#
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
#creamos un menú a base de elif y un bucle que lo englobe
lista_Martín=[]

# me niego a encadenar todo en un mismo print
print("Aquí tiene las opcionnes disponibles del menú: \n")
print("1. Añadir número al final")
print("2. Añadir número en una posición")
print("3. Longitud de la lista")
print("4. Eliminar el último número")
print("5. Eliminar un número")
print("6. Contar números")
print("7. Posiciones de un número")
print("8. Mostrar números")
print("9. Salir")

# realizamos un bucle que repita el proceso de selección del menú y dentro de este realizamos todos los opernados necesarios
# utilizamos ,remarcando los dados en la unidad, .pop, .count y .index.
salida=int(input("Introduce lo que desees hacer con la lista: "))
while salida!=9:
    
    if salida==1:
        valor=int(input("Introduce el valor que desees añadir al finalde la lista: "))
        lista_Martín.append(valor)
        salida=int(input("Introduce lo que desees hacer con la lista: "))

    elif salida==2:
        valor= int(input("Dime un valor: "))
        posición=int(input("Introduce la posición que desees: "))
        salida=int(input("Introduce lo que desees hacer con la lista: "))

    elif salida == 3:
        print("Longitud de la lista: " ,len(lista_Martín))
        salida=int(input("Introduce lo que desees hacer con la lista: "))

    elif salida == 4:
        if len(lista_Martín)>0:
            print("El elemento que vamos a eliminar es ",lista_Martín.pop()," y lo borramos.")
        else:
            print("No hay nada en la lista")
        salida=int(input("Introduce lo que desees hacer con la lista: "))

    elif salida == 5:
        pos = int(input("Dime una posición (empezando por 1):"))
        if pos > len(lista_Martín):
            print("Posición incorrecta")
        else:
            print("El elemento es ",lista_Martín.pop(pos - 1)," y lo borramos." )
        salida=int(input("Introduce lo que desees hacer con la lista: "))

    elif salida == 6:

        valor = int(input("Dime un número:"))
        print("El número ",valor," aparece veces en la lista.",lista_Martín.count(valor))
        salida=int(input("Introduce lo que desees hacer con la lista: "))

    elif salida == 7:
        valor = int(input("Dime un número para comprobar sus posiciones dentro de la lista:"))
        posición = 0
        print("Posiciones: ",end="")
        for i in range(0,lista_Martín.count(valor)):
            posición = lista_Martín.index(valor,posición)
            posición +=1
            print(posición," ",end="")
        print()
        salida=int(input("Introduce lo que desees hacer con la lista: "))

    elif salida == 8:
        for valor in lista_Martín:
            print(valor," ",end="")
        print()
        salida=int(input("Introduce lo que desees hacer con la lista: "))


    else:
        print("Valor no válido, introdúzcalo de nuevo.")
        salida=int(input("Introduce lo que desees hacer con la lista: "))


