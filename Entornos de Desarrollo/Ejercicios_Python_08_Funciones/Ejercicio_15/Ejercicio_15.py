# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 15: Vamos a realizar un programa similar al anterior para trabajar con una cola.
#               Una cola es una estructura de datos que nos permite guardar un conjunto de variables.
#               La característica fundamental es que el primer elemento que se añade al conjunto
#               es el primero que se puede sacar.
#               En realidad, nos sirven todas las funciones del ejercicio anterior excepto la función
#               SacarDeLaCola que es la que tienes que modificar.
# ****************************************************************************************


import Cola

colaMartín = []
seguirMartín = True
while seguirMartín:
    print("1.- Añadir elemento a la cola")
    print("2.- Sacar elemento de la cola")
    print("3.- Longitud de la cola")
    print("4.- Mostrar cola")
    print("5.- Salir")
    opcionMartín = int(input())
    if opcionMartín == 1:
        elemMartín = input("Dame la cadena para añadir a la cola:")
        Cola.AddCola(elemMartín, colaMartín)
    elif opcionMartín == 2:
        print(Cola.SacarDeLaCola(colaMartín))
    elif opcionMartín == 3:
        print("Longitud: ", Cola.LongitudCola(colaMartín))
    elif opcionMartín == 4:
        Cola.EscribirCola(colaMartín)
    elif opcionMartín == 5:
        print("Saliendo")
        seguirMartín = False
    else:
        print("Opción incorrecta")

