# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 7: Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco 
#              enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule 
#              lista3=lista1+lista2.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
# denominamos las listas
lista1_Martín=[]
lista2_Martín=[]
lista3_Martín=[]
# realizamos dos bucles para las dos primeras listas

for i in range (5):
    valor=int(input("Introduce un valor para la lista 1: "))
    lista1_Martín.append(valor)
print("\n")

for j in range (5):
    valor=int(input("Introduce un valor para la lista 2: "))
    lista2_Martín.append(valor)
print("\n")    
    
# realizamos un bucle para nuestra tercera lista
# donde sumaremos los valores de  las listas anteriores uno a uno


for k in range (5):
    #creamos la variable suma, la cual sumará los valores de las listas,
    # después lo añadiremos a la lista 3
    suma=lista2_Martín[k]+lista1_Martín[k]
    lista3_Martín.append(suma)
print("\n")
print("Su lista 3 es: ",lista3_Martín)