# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 14: Vamos a crear un programa para trabajar con una pila.
#               Una pila es una estructura de datos que nos permite guardar un conjunto de variables.
#               La característica fundamental es que el último elemento que se añade al conjunto
#               es el primero que se puede sacar.
#               Para representar una pila vamos a utilizar una lista de cadenas de caracteres.
#               Vamos a crear varias funciones para trabajar con la pila:
#               1. LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
#               2. EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
#               3. EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
#               4. AddPila: Función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila,
#                          si no está llena. Si está llena, muestra un mensaje de error.
#               5. SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila.
#                                 Si la pila está vacía, muestra un mensaje de error.
#               6. EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
#               Crea un programa principal que nos permita usar las funciones anteriores, que nos muestre un menú,
#               con las siguientes opciones:
#               1. Añadir elemento a la pila
#               2. Sacar elemento de la pila
#               3. Longitud de la pila
#               4. Mostrar pila
#               5. Salir
# ****************************************************************************************


import Pila

pilaMartín = []
seguirMartín = True
while seguirMartín:
    print("1.- Añadir elemento a la pila")
    print("2.- Sacar elemento de la pila")
    print("3.- Longitud de la pila")
    print("4.- Mostrar pila")
    print("5.- Salir")
    opcionMartín = int(input())
    if opcionMartín == 1:
        elementoMartín = input("Dame la cadena para añadir a la pila:")
        Pila.AddPila(elementoMartín, pilaMartín)
    elif opcionMartín == 2:
        print(Pila.SacarDeLaPila(pilaMartín))
    elif opcionMartín == 3:
        print("Longitud: ", Pila.LongitudPila(pilaMartín))
    elif opcionMartín == 4:
        Pila.EscribirPila(pilaMartín)
    elif opcionMartín == 5:
        print("Saliendo")
        seguirMartín = False
    else:
        print("Opción incorrecta")
