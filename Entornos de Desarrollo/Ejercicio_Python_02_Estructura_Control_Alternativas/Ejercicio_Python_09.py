# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*************************************
# Ejercicio 9: Algoritmo que pida tres números y los muestre ordenados (de mayor
#              a menor)
# ******************************************************************************
#

# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Deberá introducir tres números para ordenarlos de mayor a menor.")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

num_1 = float(input("Introduce aquí el primer número: "))

num_2 = float(input("Introduce aquí el primer número: "))

num_3 = float(input("Introduce aquí el primer número: "))

# Resolvemos con condicionales.

if num_1>num_2:
    if num_1>num_3:
        if num_2>num_3:
            print("Su orden de mayor a menor sería: ",num_1,">",num_2,">", num_3)
        else:
            print("Su orden de mayor a menor sería: ",num_1,">",num_3,">", num_2)
    else:
        print("Su orden de mayor a menor sería: ",num_3,">",num_1,">", num_2)
else:
    if num_2>num_3:
        if num_1>num_3:
          print("Su orden de mayor a menor sería: ",num_2,">",num_1,">", num_3)
        else:
          print("Su orden de mayor a menor sería: ",num_2,">",num_3,">", num_1)
    else:
        print("Su orden de mayor a menor sería: ",num_3,">",num_2,">", num_3)