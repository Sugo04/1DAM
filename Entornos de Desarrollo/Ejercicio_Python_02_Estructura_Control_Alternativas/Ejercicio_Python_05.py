# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 5: Escribe un programa que pida un nombre de usuario y una contraseña y 
#              si se ha introducido “pepe” y “asdasd” se indica “Has entrado 
#              al sistema”, sino se da un error.
# **********************************************************************************
#

# Mostramos con un mensaje en pantalla lo que deberá de hacer el usuario, "pepe", 
# con contraseña "asdasd".

print("Introduzca su nombre de usuario y contraseña.")

# indicamos co mensajes a pantalla, dónde debe de introducir cada valor.

usuario= input("Intrduzca aquí su nombre de usuario: ")
contraseña= input("Introduzca aquí su contraseña: ")

if usuario=="pepe":
    if contraseña == "asdasd":

        print("Has entrado al sistema")
else: 
    print("Error")
