# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*************************************
# Ejercicio 8: Algoritmo que pida dos números ‘nota’ y ‘edad’ y un 
#              carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota 
#              es mayor o igual a cinco, la edad es mayor o igual a 
#              dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo,
#              pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se 
#              cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
# ******************************************************************************
#
# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Deberá introducir, su nota, edad y sexo para saber si es aceptado.")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.

nota = float(input("Introduce aquí tu nota: "))

edad = int(input("Introduce aquí tu edad: "))

sexo= int(input("Introduce el número que corresponde a tu sexo: 1-Masculino, 2-Femenino: "))

# realizamos un condicional para asegurar que introduce valores como 1 o 2.
if sexo == 1:
    sexo = "M"
elif sexo == 2:
    sexo = "F"
else:
    print("No válido")
    sexo= int(input("Introduce el número que corresponde a tu sexo: 1-Masculino, 2-Femenino: "))
# realizamos el condicional conveniente y mostramos el resultado en pantalla
if nota>5 and edad>=18 and sexo == "F":
   print("ACEPTADA")
elif nota>5 and edad>=18 and sexo == "M" :
    print("POSIBLE")
else :
    if sexo == "F" :
        print("NO ACEPTADA")
    elif sexo == "M" :
        print("NO ACEPTADO")
    else:
        print("Ha introducido un valor no válido para el apartado 'sexo' dos veces, no se ha podido ",
              "tramitar su solicitud")
