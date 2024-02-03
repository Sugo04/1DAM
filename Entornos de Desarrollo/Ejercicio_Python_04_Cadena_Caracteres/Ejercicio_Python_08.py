# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 8: Realizar un programa que lea una cadena por teclado y convierta las 
#              mayúsculas a minúsculas y viceversa.
# **********************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

#pedimos datos

cadena_Martín=str(input("Introduzca la cadena que desee cambiar sus mayúsculas y minúsuclas: "))

# Devolvemos imprmiendo con mayúsculas las múscullas y minúsculas las mayusculas

print(cadena_Martín.swapcase())