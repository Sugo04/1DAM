# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************
# Ejercicio 19: Escribe un programa que pida un número entero entre uno y doce e imprima el 
#               número de días que tiene el mes correspondiente.
# *******************************************************************************************
#
 
# Mostramos con un mensaje en pantalla lo que el usuario deberá de hacer.

print("Deberá de introducir un número correspondiente a uno de los meses del año.\n",
      "Es decir, un número entero entre 1 y 12. Se le devolverá el número de días de dicho mes." )

# Mostramos con un mensaje donde deberá de introducir el dato

mes= int(input("Introduzca aquí el número del mes del que desea conocer sus días: ")) 

# Agregamos los días de cada mes. Usaremos una lista para darle el valor
# numérico de su último día a cada mes, como en el ejercicio 13.
# El primer dígito será cero para que Enero corresponda con el 1.
# Tomamos el supuesto de un año no bisiesto.

numero_mes = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# Realizamos un condicional con el que mostramos las soluciones
if mes<1 or mes>12:
    print("Has introducido un número incorrecto.")

else: 
    
    if numero_mes==2:
        print("Hay que tener en ceunta que tomamos un año no bisiesto como nuestro supuesto.\n",
              "En otro caso Febrero tendría 29 días.")
    numero_dias_mes= numero_mes[mes-1]
    print("El ",mes,"º mes tiene ",numero_dias_mes," días")