# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO************************************************
# Ejercicio 3: Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir 
#              la suma y la media de todos los números introducidos.
# ******************************************************************************************
#

# Mostramos al usuario lo que debe de hacer con un mensaje a pantalla.

print("Deberá de introducir tantos números como desee, se le devolverá la suma y media.",
      "Para que el programa pare, deberás de introducir el número 0.")

# Realizamos el bucle agregando un lector, un contador, y suma.
# Y debermos de inicializar un contador, el cual nombraremos como i. Definimos también el lector num.
# También deberemos de añadir un "contador" que denominaremos suma

num_Martín= float(input("Introduce un número (0 para terminar): "))

i_Martín= 1
suma_Martín = 0+num_Martín

while (num_Martín!=0):

    i_Martín = i_Martín+1
    num_Martín= float(input("Introduce un número (0 para terminar): "))
    suma_Martín=suma_Martín+num_Martín

# Ahora haremos la media de la suma de todos esos números.
if num_Martín==0:

    i_Martín=i_Martín-1

media_Martín= float(suma_Martín/i_Martín)

# Mostramos el resultado con un mensaje en pantalla.

print("La suma  de todos los números es: ",suma_Martín,"\n"
      ,"Y la media es: ", media_Martín,".")

