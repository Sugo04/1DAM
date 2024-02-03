# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 5: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
#              en caso contrario, el programa termina cuando se introduce un espacio.
# **********************************************************************************************
#

# Mostramos con un mensaje en pantalla las instruccionees para el usuario

print("Deberá de introducir cadenas de 1 solo carácter (letra).\n",
      "Se le devolverá si es una vocal o no. Para finalizar pulse 'SPACE' ")
# Con un mensaje mostramos dónde deseamos que el usuario introduzca el carácter.

cadena_Martín=(input("Introduzca aquí su cadena (pulse 'SPACE' para finalizar): "))

vocal_Martín = ["A","a","E","e","I","i","O","o","U","u"]

if cadena_Martín in vocal_Martín :
        print("VOCAL")

elif cadena_Martín==" ":
        print("Fin operación")

else:
        print("CONSONANTE")
# Realizamos un bucle para dar con la solución, finalizará cuando dejemos un espacio.

while cadena_Martín!=" ":

    # Con un mensaje mostramos dónde deseamos que el usuario introduzca el carácter.

    cadena_Martín= str(input("Introduzca aquí su cadena (pulse 'SPACE' para finalizar): "))

    # realizamos un bucle para acerciorarnos que el usuario solo introduce 1 carácter.

    

    # realizamos un condiconal para comprobar el resultado

    if cadena_Martín in vocal_Martín :
        print("VOCAL")

    elif cadena_Martín==" ":
        print("Fin operación")

    else:
        print("CONSONANTE")
    


    

