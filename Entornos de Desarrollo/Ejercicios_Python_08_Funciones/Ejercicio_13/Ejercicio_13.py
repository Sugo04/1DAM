# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 13: Queremos crear un programa que trabaje con fracciones a/b.
#               Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.
#               Vamos a crear las siguientes funciones para trabajar con fracciones:
#               1. Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador.
#                                 Cuando leas una fracción debes simplificarla.
#               2. Escribir_fracción: Esta función escribe en pantalla la fracción.
#                                     Si el dominador es 1, se muestra sólo el numerador.
#               3. Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
#               4. Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir
#                                         numerador y dominador por el MCD del numerador y denominador.
#               5. Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de
#                                   las dos fracciones. La suma de dos fracciones es otra fracción cuyo
#                                   numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la
#                                   fracción resultado.
#               6. Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2.
#                                    Se debe simplificar la fracción resultado.
#               7. Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello
#                                         numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la
#                                         fracción resultado.
#               8. Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello
#                                       numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la
#                                       fracción resultado.
#               Crea un programa que utilizando las funciones anteriores muestre un menú.
# ****************************************************************************************


import Fracciones

seguir_Martín = True
while seguir_Martín:
    print("1.- Sumar dos fracciones")
    print("2.- Restar dos fracciones")
    print("3.- Multiplicar dos fracciones")
    print("4.- Dividir dos fracciones")
    print("5.- Salir")
    
    opcion_Martín = int(input("Introduce lo que desee hacer: "))
    print("\n")
    
    if opcion_Martín >= 1 and opcion_Martín <= 4:
        print("Fracción 1:")
        num1_Martín, den1_Martín = Fracciones.LeerFraccion()
        print("\n")
        print("Fracción 2:")
        num2_Martín, den2_Martín = Fracciones.LeerFraccion()
        print("\n")

    if opcion_Martín == 1:
        numr_Martín, denr_Martín = Fracciones.SumarFracciones((num1_Martín, den1_Martín), (num2_Martín, den2_Martín))
        Fracciones.EscribirFraccion((numr_Martín, denr_Martín))
        print("\n")
    elif opcion_Martín == 2:
        numr_Martín, denr_Martín = Fracciones.RestarFracciones((num1_Martín, den1_Martín), (num2_Martín, den2_Martín))
        Fracciones.EscribirFraccion((numr_Martín, denr_Martín))
        print("\n")
    elif opcion_Martín == 3:
        numr_Martín, denr_Martín = Fracciones.MultiplicarFunciones((num1_Martín, den1_Martín), (num2_Martín, den2_Martín))
        Fracciones.EscribirFraccion((numr_Martín, denr_Martín))
        print("\n")
    elif opcion_Martín == 4:
        numr_Martín, denr_Martín = Fracciones.DividirFracciones((num1_Martín, den1_Martín), (num2_Martín, den2_Martín))
        Fracciones.EscribirFraccion((numr_Martín, denr_Martín))
        print("\n")
    elif opcion_Martín == 5:
        seguir_Martín = False
    else:
        print("Opción incorrecta")
