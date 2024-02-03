# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 5: Crea una función "calcularMaxMin" que recibe una lista con valores numéricos
#              y devuelve el valor máximo y el mínimo. Crea un programa que pida números
#              por teclado y muestre el máximo y el mínimo, utilizando la función anterior.
# ****************************************************************************************


import calcularMaxMin
import random

nMartín = int(input("Introduce el número de datos que desea en su lista: "))
listaMartín = []

for iMartín in range(0, nMartín):
    listaMartín.append(random.random())

print(f"El máximo y el mínimo son {calcularMaxMin.maxmin(listaMartín)}\n")
