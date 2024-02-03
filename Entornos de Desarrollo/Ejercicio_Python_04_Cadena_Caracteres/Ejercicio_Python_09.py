# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*********************************************
# Ejercicio 9: Realizar un programa que compruebe si una cadena contiene una subcadena.
#              Las dos cadenas se introducen por teclado.
# **************************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# pedimos los datos

caracter_Martín=str(input("aqui la palabra o cadena de palabras: "))

subcadena_Martín=str(input("aquí la cadena que deseas comprobar si aparece: "))

#realizamos un bucle que compuebe que la subcadena está dentro de la cadena

if subcadena_Martín in caracter_Martín:
    
    print("Sí que aparece su subcadena en la cadena de carácteres o carácter.")

else:
    print("No aparece ninguna subcadena paracida en si caracter o cadena de caracteres.")