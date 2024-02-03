# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 6: Realizar un programa que dada una cadena de caracteres por 
#              caracteres, genere otra cadena resultado de invertir la primera.
# **********************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# pedimos datos
cadena_Martín=str(input("Introduzca aquí la cadena que desee invertir: "))

# invertimos la cadena que nos han dado y mostramos la solución
inversa_Martín=cadena_Martín[::-1]

print("La cadena resultante de revertir ",cadena_Martín," es: ",inversa_Martín)