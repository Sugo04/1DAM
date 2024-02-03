# Alumno: Héctor Martín Ortega
#
# **********************************************************************************************
# Ejercicio 05: Escribir un programa que implemente una agenda. En la agenda se podrán 
#               guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
#
#   Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar 
#   el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se 
#   encuentra, debe permitir ingresar el teléfono correspondiente.
#
#   Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres 
#   comiencen por dicha cadena.
#
#   Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
#
#   Listar: Nos muestra todos los contactos de la agenda.
#
#   Implementar el programa con un diccionario. 
# ***********************************************************************************************
#

# colocamos el diccionario fuera así no se reinicia constantemente e iniciamos un bucle.

agenda_Martín={}

while True:
    
    print("-----------MENÚ AGENDA-----------\n")
    print("1-Añadir/Modificar")
    print("2-Buscar")
    print("3-Borrar/Eliminar")
    print("4-Listar/Mostrar")
    print("5-Salir")
    
    # seguir nos sirve para mantener el bucle abierto.
    seguir=int(input("Introduce el número correspondiente a la operación que deseas realizar: "))
    
    if seguir == 1:
        nombre = str(input("Introduce el nombre de la persona: "))
        if nombre in agenda_Martín:
            print(f"El número de {nombre} es {agenda_Martín[nombre]}.")
            # realizamos un condicional para comprobar si está agendado ya o no.
            modificar = input("¿Desea modificar el número de teléfono? (S/N): ")
            if modificar.upper() == "S":
                nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
                agenda_Martín[nombre] = nuevo_telefono
                print("Número de teléfono modificado correctamente.")
        else:
            numero= int(input("Introduce tu número de teléfono: "))
            agenda_Martín[nombre] = numero
            print("Contacto guardado.")
            
    elif seguir == 2:
        buscar = input("Introduce el nombre a buscar: ")
        for nombre, numero in agenda_Martín.items():
            if nombre.startswith(buscar): #no funciona y no sé por qué (me sucede solo a mí a usted debería funcionarle)
                print(f"{nombre}: {numero}")
                
    elif seguir == 3:
        nombre = input("Ingrese el nombre a borrar: ")
        if nombre in agenda_Martín:
            confirmacion = input(f"¿Está seguro de que desea borrar {nombre} de la agenda? (S/N): ")
            if confirmacion.upper() == "S":
                del agenda_Martín[nombre]
                print("Contacto borrado correctamente.")
        else: 
            print("No existe tal nombre entre sus contactos")
            
    elif seguir == 4:
        for nombre, telefono in agenda_Martín.items():
            print(f"{nombre}: {telefono}")
            
    elif seguir == 5:
        print("Adiós")
        break
        
    else:
        print("Dato erróneo, inténtelo de nuevo.")