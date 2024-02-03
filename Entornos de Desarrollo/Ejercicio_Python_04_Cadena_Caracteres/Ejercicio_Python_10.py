# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO********************************************
# Ejercicio 10: Introducir una cadena de caracteres e indicar si es un palíndromo. 
#               Una palabra palíndroma es aquella que se lee igual adelante que atrás.
# **************************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# pedimos datos

cadena_Martín=str(input("Introduzca aquí su cadena: "))

#quitamos los espacios de la cadena y la convertimos a minúsculas todo

cadena_Martín=str(cadena_Martín.lower())
cadena_Martín=str(cadena_Martín.replace(" ",""))

# Realizamos la inversa leyendo desde atrás

inversa_Martín=str(cadena_Martín[::-1])

# realizamos un bucle que nos otorgue la solución según sean iguales o no
if inversa_Martín==cadena_Martín:
    
    print("Se trata de un palíndromo.")
    
else:
    
    print("No es un palíndromo")