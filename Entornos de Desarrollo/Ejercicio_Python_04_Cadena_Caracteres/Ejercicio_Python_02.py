# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 2: Realizar un programa que comprueba si una cadena leída por teclado 
#              comienza por una subcadena introducida por teclado.
# **********************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# Obtenemos los datos deseados
caracter_Martín=str(input("aqui la palabra o cadena de palabras: "))

subcadena_Martín=str(input("aquí la cadena que deseas comprobar si aparece en primer lugar: "))

# comprobamos si la cadena empieza con la subcadena y devolvemos el resultado con un mensaje
if caracter_Martín.startswith(subcadena_Martín):
    
    print("Sí que empieza su subcadena en la cadena de carácteres o carácter.")

else:
    print("No aparece su subcadena como primer componente de su cadena.")