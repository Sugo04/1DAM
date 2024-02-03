# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************
# Ejercicio 6: Programa que lea una cadena por teclado y compruebe si 
#              es una letra mayúscula.
# **********************************************************************
#

# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Introduzca una letra (solo una) y nosotros le diremos si es mayúscula")

# Indicamos al usuario donde debe de introducir la variable con un mensaje
# a pantalla.

letra = input("Introduzca aquí la letra: ")

if letra.isupper():
    print("Es mayúscula.")
else :
    print("No es mayúscula.")