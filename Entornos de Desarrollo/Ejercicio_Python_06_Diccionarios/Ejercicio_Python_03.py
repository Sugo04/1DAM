# Alumno: Héctor Martín Ortega
#
# ******************************************************************************************
# Ejercicio 03: Vamos a crear un programa en python donde vamos a declarar un diccionario 
#               para guardar los precios de las distintas frutas. El programa pedirá el 
#               nombre de la fruta y la cantidad que se ha vendido y nos mostrará el 
#               precio final de la fruta a partir de los datos guardados en el diccionario.
#               Si la fruta no existe nos dará un error. Tras cada consulta el programa nos 
#               preguntará si queremos hacer otra consulta.
# ******************************************************************************************
#
# (Solo agregamos el apellido a los diccionarios para mayor legibilidad. Además lo indica el enunciado.)

# vamos a crear la lista denominada frutas vacía, en ella el ususario debera
# de introducir el nombre la fruta y su precio kg.

precioFrutas_Martín={}
cantidadFrutas=int(input("¿Cuántos tipos de fruta se venden en tu frutería?: "))

for i in range(cantidadFrutas):
    
    nombresFrutas=str(input("Introduce el nombre de la fruta: "))
    
    precioFrutas_Martín[nombresFrutas]=int(input("Introduce el precio de {{nombresFrutas}} por unidad: "))
    
while True:
    # solicitamos al usuario el nombre de la fruta de la que quiere introducir la cantidada deseada. Hacemos un bucle 
    # para comprobar si existe dentro del diccionario. Y otro por si desea salir
    
    fruta = input("Ingresa el nombre de la fruta (o 'salir' para terminar): ")
    
    if fruta.lower() == 'salir':
        break

    if fruta in precioFrutas_Martín:

        cantidad = int(input(f"Ingresa la cantidad de {fruta} vendida: "))

        # Calculamos el precio final de la fruta (hemos pedido el precio unidad) y mostramos la solución con un mensaje a pantalla.
        precio_final = precioFrutas_Martín[fruta] * cantidad

        print(f"El precio final de {cantidad} {fruta} es: {precio_final} euros\n")
    else:
        # Mandamos un mensaje a pantalla de error si la fruta no se encuentra entre las que el usuario nos ha proporcionado.
        print(f"Error: La fruta '{fruta}' no está en el diccionario de precios.\n")