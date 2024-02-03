# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 5: Hacer un programa que inicialice una lista de números con valores 
#              aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
import random
#consideramos que son 10 valores los de la lista

lista_Martín=[]
for i in range(10):
    valor=random.random()
    lista_Martín.append(valor)
    
lista_Martín.sort()
print(lista_Martín)