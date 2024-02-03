# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 09: Escribe un programa en python que lea el fichero json pedidos.json con 
#               datos de órdenes, deberá mostrar en la terminal todos las órdenes de 
#               pedidos que no se hayan entregado.
# ****************************************************************************************


import json

# Abrimos el archivo pedidos.json y cargamos los datos de este en otra variable
with open("pedidos.json") as archivo_martín:
    datos_pedidos_martín = json.load(archivo_martín)
    
# Debemos mostrar solo los pedidos cuyo envío no haya sido realizado (delivery=false).
print("Los órdenes de pedidos no entregados son: \n")

# commprobamos en el fichero que si el pedido no se ha entregado y mostramos sus datos uno por uno comprobando si existen o no (Como con Toppings)
for pedido_martín in datos_pedidos_martín['ordenes']:
    if not pedido_martín['delivery']:
        
        orden_martín = json.dumps(pedido_martín)
        print(f"Tamaño: {pedido_martín['tamano']}\n")
        print(f"Precio: {pedido_martín['precio']}\n")
        
        if not pedido_martín['toppings']:
            print("Toppings: -")
        else:
            print(f"Toppings: {pedido_martín['toppings']}")
            
        if pedido_martín['queso_extra']:
            print("Queso extra: Sí")
            
        print(f"Cliente: {pedido_martín['cliente']['nombre']}\n",
              f"Tlfo:    {pedido_martín['cliente']['telefono']}\n",
              f"Correo:  {pedido_martín['cliente']['correo']}")
