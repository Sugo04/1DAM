# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 4: Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
#              números a introducir). El programa debe informar de cuantos números introducidos 
#              son mayores que 0, menores que 0 e iguales a 0.
# **********************************************************************************************
#

# Mostramos al usuario lo que debe de hacer con un mensaje a pantalla.

print("Deberá de introducir la cantidad de números que desea introducir.\n",
      "El prgrama deberá devolver la cantidad de número mayores, menores e iguales a 0.")

# 
num_Martín= float(input("Introduce la cantidad de números que desea introducir: "))

i_Martín= 0
mayores_Martín=0
menores_Martín=0
iguales_Martín=0

while (i_Martín!=num_Martín):

    i_Martín = i_Martín+1
    num_2_Martín= float(input("Introduce un número: "))

    if num_2_Martín<0:
        menores_Martín  = menores_Martín+1

    elif num_2_Martín==0:
        iguales_Martín = iguales_Martín+1

    else:
        mayores_Martín=mayores_Martín+1
    

# Ahora haremos la media de la suma de todos esos números.

# Mostramos el resultado con un mensaje en pantalla.

print("La cantidad de números mayores a 0 son: ",mayores_Martín,"\n")

print("La cantidad de números menores a 0 son: ",menores_Martín,"\n")

print("La cantidad de números iguales a 0 son: ",iguales_Martín,"\n")