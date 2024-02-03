# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*************************************
# Ejercicio 13: Escribe un programa que pida una fecha (día, mes y año) y 
#               diga si es correcta.
# ******************************************************************************
#

# Mostramos con un mensaje en pantalla lo que el usuario debe de hacer

print("Deberá introducir el día mes y año que desee para saber si esa fecha es correcta.")

# Indicamos al usuario donde debe de introducir las variables con un mensaje
# a pantalla.
dia = int(input("Introduce aquí el día: "))
mes = int(input("Introduce aquí el mes (numéricamente): "))
Año = int(input("Introduce aquí el año: "))

# Agregamos los días de cada mes. Tras una investigación de cómo, usaremos 
# una lista para darle el valor numérico de su último día a cada mes.
# El primer dígito será cero para que Enero corresponda con el 1.

dias_mes = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# usamos condicional para comprobar que todo sea cierto o no y para 
# dar los valores correctos a Febrero

if  Año%4 == 0 and Año%100 != 0  or Año%400 == 0:
    
    dias_mes[2] = 29

else :
    
   dias_mes[2] = 28
   
if mes<1 or mes>12 or dia<1 or dia>dias_mes[mes]:
    
    print("La fecha es incorrecta")
   
else:
    
    print("La fecha es correcta")