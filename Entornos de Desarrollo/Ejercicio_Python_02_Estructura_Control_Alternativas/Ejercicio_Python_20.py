# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO****************************************************
# Ejercicio 20: Una compañía de transporte internacional tiene servicio en algunos países
#               de América del Norte, América Central, América del Sur, Europa y Asia. El 
#               costo por el servicio de transporte se basa en el peso del paquete y la zona
#               a la que va dirigido. Parte de su política implica que los paquetes con un peso
#               superior a 5 kg no son transportados, esto por cuestiones de logística y de 
#               seguridad. Realice un algoritmo para determinar el cobro por la entrega de 
#               un paquete o, en su caso, el rechazo de la entrega.
# **********************************************************************************************
#
 
 # Mostramos con un mensaje lo que el usuario debe de hacer.
 
print("Deberá de introducir el peso del paquete y a dónde quiere enviarlo. Se le dirá el importe que deberá abonar.")

# Mostramos con un mensaje en pantalla dónde deben de introducirse los datos.
print("los destinos a los que puede enviar un paquete son: \n",
                                "América del norte\n",
                                "América Central\n",
                                "América del Sur\n",
                                "Europa\n",
                                "Asia\n",)
destino = input("Introduzca aquí el nombre del destino: " )
	

peso_kg = float(input("Introduzca el peso de su paquete en kg: "))

# colocamos el peso en gramos 
peso_gramos= peso_kg*1000

# introducimos un condicional para obtener el precio por gramo en cada lugar.

if destino== "América del Norte":
    costo_gramo = 24
elif destino=="América Central":
    costo_gramo = 20
elif destino=="América del Sur":
    costo_gramo = 21
elif destino=="Europa":
    costo_gramo = 10
elif destino=="Asia":
    costo_gramo = 18
else:
    print("El lugar seleccionado no es válido.")
    
# hacemos un condicional, mostrando la solución.

if peso_kg>5 or peso_kg<0:
    
    print("No se permiten paquetes de más de 5Kg, se rechazará su envio por motivos de seguridad")
    
else: 
    
    coste= costo_gramo*peso_gramos
    print("El coste del envio de su paquete será de: ",coste," euros.")
    
    

