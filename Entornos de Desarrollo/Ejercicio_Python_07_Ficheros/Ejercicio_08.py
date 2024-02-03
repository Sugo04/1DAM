# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 08: Escribe un programa en python que lea el fichero json colores.json con 
#               datos de colores, deberá mostrar en la terminal todos los nombres de 
#               colores, sus códigos rgba y hexadecimal respectivamente.
# ****************************************************************************************

#importamos la libreria json para leer el archivo que deseeamos
import json

# Abrimos el archivo colores.json y cargamos los datos de este en otra variable
with open("colores.json") as archivo_martín:
    datos_colores_martín = json.load(archivo_martín)
    
# Realizamos un bucle que nos muestre todos los colores dentro del nuevo datos_colores_martín que contiene 
print("\n")
print("Nombre - RGBA - Hexadecimal")
print("\n")

for color_martín in datos_colores_martín['colors']:
    nombre_color_martín = color_martín['color']
    code_rgba_martín = color_martín['code']['rgba']
    code_hexadecimal_martín = color_martín['code']['hex']
    
    print(f"{nombre_color_martín}: {code_rgba_martín} || {code_hexadecimal_martín}")
    print("\n")

