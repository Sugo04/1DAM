# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 5: Si tenemos una cadena con un nombre y apellidos, realizar un programa
#              que muestre las iniciales en mayúsculas.
# **********************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# obtenemos el nombre del usuario 

nombre_Martín=str(input("Introduzca aquí su nombre completo: "))

# Devolvemos imprimiendo en mayúscula el primer caracter de cada palabra

print(nombre_Martín.title())