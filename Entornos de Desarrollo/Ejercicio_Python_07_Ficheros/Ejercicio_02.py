# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 02: Escribir una función que pida un número entero entre 1 y 10, lea el 
#               fichero primerapellido-n.txt con la tabla de multiplicar de ese número, 
#               donde n es el número introducido, y la muestre por pantalla. Si el fichero 
#               no existe debe mostrar un mensaje por pantalla informando de ello.
# ****************************************************************************************

import locale
locale.getpreferredencoding

# solicitamos al usuario el numero del que desea conocer su tabla de multiplicar y realizamos un bucle 
# para verificar su pertenencia al intervalo 1-10.

num_martín = int(input("Introduce el número que desees (que se encuentre entre 1 y 10): "))
while num_martín < 1 or num_martín > 10:
    num_martín = int(input("Introduce el número que desees (que se encuentre entre 1 y 10): "))

# abrimos el fichero martín solo si existe, sino, nos devolverá un mensaje de error.
fichero_martín = f"martín-{num_martín}.txt"

try: 
    with open(fichero_martín, "r") as archivo_martín:
        contenido_martín = archivo_martín.read()
        print(f"Tabla del {num_martín}:\n{contenido_martín}")
except FileNotFoundError:
    print('No existe el fichero con la tabla del', num_martín)


