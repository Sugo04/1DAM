# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*******************************************
# Ejercicio 4: Crea un programa que pida al usuario dos números y muestre su división 
#              si el segundo no es cero, o un mensaje de aviso en caso contrario.
# ************************************************************************************
#

# Mostramos al usuario con un mensaje en pantalla lo que deberá de hacer.

print("Deberá de introducir dos números distintos, y se le devolverá su división siempre ",
      "y cuando el segundo no sea 0")

# Indicamos con mensajes a pantalla, dónde debe de introducir los valores numéricos.

num_1 = float(input("Introduzca el primer número (puede ser decimal): "))

num_2 = float(input("Introduzca el segundo número (No puede ser 0): "))

# Realizamos el condicional y operaciones convenientes para dar la solución con 
# un mensaje a la pantalla

if num_2==0:
    print("El segundo es 0, no se hará la división")
else:
    división = float(num_1/num_2)
    print("La solución de la división es: ", división)
