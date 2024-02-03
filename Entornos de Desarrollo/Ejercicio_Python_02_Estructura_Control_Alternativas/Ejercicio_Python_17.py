# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************
# Ejercicio 17: Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#               al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#               (dato cadena) de la cara opuesta al resultado obtenido.
# *******************************************************************************************
#
 
# Mostramos con un mensaje en pantalla lo que el usuario deberá de hacer.

print("Deberá de introducir un número correspondiente al número de caras de un dado.\n",
      "Es decir, un número entero entre 1 y 6. Se le devolverá su cara opuesta" )

# Mostramos con un mensaje donde deberá de introducir el dato

cara= int(input("Introduzca aquí el número de la cara: ")) 

# Calculamos la cara opuesta, y hacemos unos condicionales con los cuales mostramos la solución.

cara_opuesta= int(7-cara)
if cara_opuesta==1:
    print("La cara opuesta de ",cara," es: uno.")
elif cara_opuesta==2:
   print("La cara opuesta de ",cara," es: dos.")
elif cara_opuesta==3:
   print("La cara opuesta de ",cara," es: tres.")
elif cara_opuesta==4:
    print("La cara opuesta de ",cara," es: cuatro.")
elif cara_opuesta==5:
    print("La cara opuesta de ",cara," es: cinco.")
elif cara_opuesta==6:
    print("La cara opuesta de ",cara," es: seis.")
else:
    print("ERROR: número incorrecto")