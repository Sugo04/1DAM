# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 9: Crea una función que calcule el MCD de dos números por el método de Euclides.
#              El método de Euclides es el siguiente:
#              1. Se divide el número mayor entre el menor.
#              2. Si la división es exacta, el divisor es el MCD.
#              3. Si la división no es exacta, dividimos el divisor entre el resto obtenido
#                 y se continúa de esta forma hasta obtener una división exacta, siendo el
#                 último divisor el MCD.
#              Crea un programa principal que lea dos números enteros y muestre el MCD.
# ****************************************************************************************

import Euclides
numero1Martín = int(input("Introduce el primer numero:"))
numero2Martín = int(input("Introduce el segundo numero:"))
print(f"El mcd es  {Euclides.mcd(numero1Martín,numero2Martín)}")
