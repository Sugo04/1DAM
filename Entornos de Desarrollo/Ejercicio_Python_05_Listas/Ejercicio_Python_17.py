# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 17: Crear un programa que añada números a una lista hasta que introducimos un 
#              número negativo. A continuación debe crear una nueva lista igual que la 
#              anterior pero eliminando los números duplicados. Muestra esta segunda lista 
#               para comprobar que hemos eliminados los duplicados.
# ****************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
# usamos un while al no tener limite en la lista

lista_Martín=[]
lista2_Martín=[]
print("----------------------------------------------------------------")
print("\n")
valor=int(input("introduzca un valor mayor 0: "))
print("\n")
#realizamos un bucle que se repita mientras nuestro valor no sea mayor a 0.
while valor>0:
    lista_Martín.append
    valor=int(input("introduzca un valor mayor 0: "))
    print("\n")
    # indicamos que aquellos que no esten en la lista dos son los que 
    # se pueden introducir.
    if valor not in lista2_Martín:
        lista2_Martín.append(valor)
    
lista2_Martín.pop()    #eliminamos el último componente que es un negativo que no necesitamos.
print("La lista sin duplicados sería: ",end="")
for valor in lista2_Martín:
    print(valor," ",end="")
print("\n")
print("----------------------------------------------------------------")