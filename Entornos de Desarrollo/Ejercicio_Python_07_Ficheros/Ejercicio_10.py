# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 10: Escribe un programa en python que lea el fichero json pedidos.json con 
#               datos de ordenes, a continuación deberá  crear otro fichero 
#               primerapellido_clientes.json con los todos los datos de los clientes.
# ****************************************************************************************

#importamos la libreria json para leer el archivo que deseeamos
import json
# cremaos una lista y un dicccionario donde guardamos los datos que metermos en el nuevo fichero
clientes_martín = {}
datos_clientes_martín = []
# Abrimos el archivo pedidos.json y cargamos los datos de este en otra variable y una lista para no perder los datos de los clientes.
with open("pedidos.json") as archivo_martín:
    datos_pedidos_martín = json.load(archivo_martín)
    
    for datos_martín in datos_pedidos_martín['ordenes']:
        datos_clientes_martín.append(datos_martín['cliente'])
        
    clientes_martín['Clientes'] = datos_clientes_martín

#creamos el nuevo archivo y lo rellenamos con la informacion obtenida
with open("martín_clientes.json", 'w') as archivo_nuevo_martín:
    json.dump(clientes_martín, archivo_nuevo_martín, indent=1)    