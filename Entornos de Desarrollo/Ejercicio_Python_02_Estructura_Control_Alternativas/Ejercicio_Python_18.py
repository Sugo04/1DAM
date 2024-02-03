# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************
# Ejercicio 18: Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el 
#               día correspondiente. Si introducimos otro número nos da un error.
# *******************************************************************************************
#
 
# Mostramos con un mensaje en pantalla lo que el usuario deberá de hacer.

print("Deberá de introducir un número correspondiente a uno de los días de la semana.\n",
      "Es decir, un número entero entre 1 y 7. Se le devolverá el nombre de ese día." )

# Mostramos con un mensaje donde deberá de introducir el dato

dia= int(input("Introduzca aquí el número del día que desea conocer: ")) 

# hacemos unos condicionales con los cuales mostramos la solución.


if dia==1:
    print("El día: ",dia,". Es lunes")
elif dia==2:
    print("El día: ",dia,". Es martes")
elif dia==3:
    print("El día: ",dia,". Es miércoles")
elif dia==4:
    print("El día: ",dia,". Es jueves")
elif dia==5:
    print("El día: ",dia,". Es viernes")
elif dia==6:
    print("El día: ",dia,". Es sábado")
elif dia==7:
    print("El día: ",dia,". Es domingo")
else:
    print("ERROR: número incorrecto")