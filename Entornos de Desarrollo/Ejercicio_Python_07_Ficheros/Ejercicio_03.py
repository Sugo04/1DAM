# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 03: Escribir una función que pida dos números n y m entre 1 y 10, lea el 
#               fichero primerapellido-n.txt con la tabla de multiplicar de ese número, 
#               y muestre por pantalla la línea m del fichero. Si el fichero no existe 
#               debe mostrar un mensaje por pantalla informando de ello.
# ****************************************************************************************

import locale
locale.getpreferredencoding

# pedimos ambos valores n y m. Y generamos un bucle para asegurarnos que sean entre 1 y 10

n_martín = int(input("Introduce el número que desees (que se encuentre entre 1 y 10): "))
m_martín = int(input("Introduce la fila que desees (que se encuentre entre 1 y 10): "))

while (n_martín < 1 or n_martín > 10) or (m_martín < 1 or m_martín > 10):
    n_martín = int(input("Introduce el número que desees (que se encuentre entre 1 y 10): "))
    m_martín = int(input("Introduce la fila que desees (que se encuentre entre 1 y 10): "))
    
# comprobamos que el archivo exista con un try catch como en ejercicios anteriores y resolvemos en 
# consecuencia

fichero_martín = f"martín-{n_martín}.txt"

try: 
    with open(fichero_martín, "r") as archivo_martín:
        # vamos a comprobar que m_martín se encuentre entre las líneas del documento
        contenido_martín = archivo_martín.readlines()
        if m_martín < 1 or m_martín > len(contenido_martín):
            print(f"El número {m_martín} se encuentra fuera de los parámetros de nuestro fichero.")     
        else:
            linea_martín = contenido_martín[m_martín - 1]
            print(f"La línea {m_martín} de nuestro fichero de la tabla de multiplicar del {n_martín} es: {linea_martín}")
except FileNotFoundError:
    print("No existe el fichero.")


