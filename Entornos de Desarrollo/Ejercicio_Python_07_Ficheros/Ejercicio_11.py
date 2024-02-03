# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 11: Escribe un programa en python que lea el fichero gazpacho.json con 
#               datos su origen e ingredientes, a continuación deberá  crear otro 
#               fichero primerapellido_ingredientes.json con los todos los datos de sus 
#               ingredientes.
# ****************************************************************************************

#importamos la libreria json para leer el archivo que deseeamos
import json
# abrimos un diccionario y una lista para guardar datos
ingredientes_martín = {}
datos_ingredientes_martín = []
#abrimos el archivo gazpacho.json y cargamos los datos de este en otra variable
with open("gazpacho.json") as archivo_martín:
    datos_pedidos_martín = json.load(archivo_martín)
    
    for datos_martín in datos_pedidos_martín['ingredientes']:
        datos_ingredientes_martín.append(datos_martín)
    
    ingredientes_martín = datos_ingredientes_martín
#creamos un archivo nuevo donde guardo lo que he recogido del otro fichero
with open("martín_ingredientes.json", 'w') as archivo_nuevo_martín:
    json.dump(datos_ingredientes_martín, archivo_nuevo_martín, indent=1)

    
