# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 4:Programa que declare una lista y la vaya llenando de números hasta que 
#             introduzcamos un número negativo. Entonces se debe imprimir el vector 
#             (sólo los elementos introducidos).
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
lista_Martín=[]
print("\n")
print("--------------------------------------------------------------")
while True:
    
    valor=int(input("Introduce el valor que desees: "))
    
    if valor == -1:
        break #detenemos el bucle.
    
    print("\n")
    lista_Martín.append(valor)

# vamos a quitar el -1 de la lista

lista_Martín.pop()
print("\n")
print(lista_Martín)
print("--------------------------------------------------------------")
print("\n")