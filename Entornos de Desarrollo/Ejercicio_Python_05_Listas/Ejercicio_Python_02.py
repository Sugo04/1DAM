# Alumno: Héctor Martín Ortega
#
# **************************************************************************************
# Ejercicio 2: Crea una lista e inicialízala con 5 cadenas de caracteres leídas por 
#              teclado. Copia los elementos de la lista en otra lista pero en orden 
#              inverso, y muestra sus elementos por la pantalla.
# **************************************************************************************
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.)

# -  buscamos que solo lea 5 valores, por eso el for _ in range (5)  -

print("\n")
print("*********************************************************************************************")
lista_Martín =[int(input("Introduce el número aquí: ")) for _ in range(5)]
print("\n")

print("****************************************************************************")
print( "Su lista de valores son: ",lista_Martín)

print("\n")

# Realizamos la lista inversa.

lista2_Martín=lista_Martín[:]
lista2_Martín.reverse()


print ("Su lista inversa de valores son: ",lista2_Martín)
print("****************************************************************************")
print("\n")

print("*********************************************************************************************")
