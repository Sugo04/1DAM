# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*********************************************
# Ejercicio 14: La asociación de vinicultores tiene como política fijar un 
#               precio inicial al kilo de uva, la cual se clasifica en tipos 
#               A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
#               producto, ésta es de un solo tipo y tamaño, se requiere determinar 
#               cuánto recibirá un productor por la uva que entrega en un embarque, 
#               considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos
#               al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 
#               2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 
#               céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la 
#               ganancia obtenida.
# ***************************************************************************************
#

# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Deberá introducir el vallor inicial de la uva, el tipo de uva, y su tamaño.\n",
      "Para saber las ganancias que se obtienen.  ")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

precio_inicial_kilo_uva = float(input("Introduce aquí el precio inicial de la uva: "))
tipo_uva = input("Introduce aquí el tipo de uva (A o B, en mayúsculas): ")
tamaño_uva = int(input("Introduce aquí el tamaño de las uvas(1-pequeño, 2-grande): "))
cantidad = float(input("Introduce los kilos de uva que vas a vender: "))
# realizamos 
if tipo_uva == "A":
    
    if tamaño_uva == 1:
        precio_kilo_uva = precio_inicial_kilo_uva+0.20
    elif tamaño_uva == 2:
        precio_kilo_uva = precio_inicial_kilo_uva+0.30
        
elif tipo_uva=="B":
    
    if tamaño_uva == 1:
        precio_kilo_uva = precio_inicial_kilo_uva-0.30
    elif tamaño_uva == 2:
        precio_kilo_uva = precio_inicial_kilo_uva-0.50

else: 
    print("Error al introducir los datos")
    
# hacemos la operación para comprobar las ganacias, y mostramos la solución

ganancias =   precio_kilo_uva*cantidad - precio_inicial_kilo_uva*cantidad

print("Las ganancias de la uva ",tipo_uva,"-",tamaño_uva, " si vendes todo serán: ",ganancias, " euros.")
