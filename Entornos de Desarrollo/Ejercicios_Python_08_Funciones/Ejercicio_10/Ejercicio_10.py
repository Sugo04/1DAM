# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 10: Escribe dos funciones que permitan calcular:
#               1. La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#               2. La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#               Escribe un programa principal con un menú donde se pueda elegir la opción de
#               convertir a segundos, convertir a horas, minutos y segundos, o salir del programa.
# ****************************************************************************************


import TiempoHS

seguirMartín = True

while seguirMartín:
    print("\n1.- Cantidad de segundos")
    print("2.- Tiempo dado en segundos")
    print("3.- Salir\n")
    opcionMartín = int(input("Introduzca según quiera hacer:"))

    if opcionMartín == 1:
        segundosMartín = int(input("introduzca los segundos: "))
        minutosMartín = int(input("introduzca los minutos: "))
        horaMartín = int(input("introduzca las horas: "))

        print(f"la cantidad de segundos son: {TiempoHS.segundos(horaMartín, minutosMartín, segundosMartín)}")
    elif opcionMartín == 2:
        segundosMartín = int(input("introduzca los segundos: "))

        print(f"Han pasado {TiempoHS.horaReal(segundosMartín)}")

    elif opcionMartín == 3:
        print("saliendo")
        seguirMartín = False
    else:
        print("Se ha equivocado.")
