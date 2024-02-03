# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 01: Escribir una función que pida un número entero entre 1 y 10 y guarde en 
#               un fichero con el nombre primer apellido-n.txt la tabla de multiplicar 
#               de ese número, done n es el número introducido.
# ****************************************************************************************

# solicitamos al usuario el numero del que desea conocer su tabla de multiplicar y realizamos un  bucle 
# para verificar su pertenencia al intervalo 1-10.

num_martín = int(input("Introduce el número que desees (que se encuentre entre 1 y 10): "))
while num_martín < 1 or num_martín > 10:
    num_martín = int(input("Introduce el número que desees (que se encuentre entre 1 y 10): "))

# abrimos el archivo martín-n.txt y guardamos los resultado en el fichero
fichero_martín = f"martín-{num_martín}.txt"
with open(fichero_martín, "w") as archivo_martín:
    for i_martín in range(11):
        archivo_martín.write(f"{num_martín}x{i_martín}={num_martín*i_martín}\n")

print("Se ha almacenado adecuadamente el archivo.")
