# Alumno: Héctor Martín Ortega
#
# ******************************************************************************************
# Ejercicio 6: Crea un programa que pida un número al usuario un número de mes (por 
#              ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del 
#              mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene
#              28 días.
# ******************************************************************************************
#
# (A los contadores y valores que no sean listas no se les nombra con el apellido con el fin de una mejor legibilidad del código.
# Aparte en el enunciado solo pide las listas con el apellido.)
# realizamos dos listas, una de caracteres y otra de valores, cada una para 
# colocar los meses y sus dias.

nombreMes_Martín=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
diaMes_Martín=[31,28,31,30,31,30,31,31,30,31,30,31]

# realizamos un mensaje apara pedir los datos como el número de mes. 
valorUsuario= int(input("Introduzca el número del mes que deseas conocer: "))
valorUsuario=valorUsuario-1

while valorUsuario<1 or valorUsuario>12:
    valorUsuario= int(input("Introduzca el número del mes que deseas conocer: "))
    

    
print(nombreMes_Martín[valorUsuario]," tiene ",diaMes_Martín[valorUsuario]," dias.")

