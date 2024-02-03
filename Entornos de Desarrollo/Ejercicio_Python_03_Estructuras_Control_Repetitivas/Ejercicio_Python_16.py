# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************************
# Ejercicio 16: Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
#               Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, 
#               calcule cuánto pagó la empresa por los N empleados.
# *******************************************************************************************************
#

# Mostramos un mensje especificando lo que se debde de hacer.

print("Deberá introducie cobrar el nombre de sus empleados, lo qu por hora, y las horas trabajadas. (Al día)",
      "Al final se le mostrará el pago total de su empresa a sus empleados.")

# colocamos una variable que nos servirá para salir del bucle.

salida_Martín=int(input("Introduzca 0 para salir, otro número para comenzar: "))
print("\n")

pagoTotal_Martín=0

contador_Martín=0

while salida_Martín!=0:

    contador_Martín=contador_Martín+1

    nombreTrabajador_Martín=str(input("Introduzca el nombre de su empleado: "))
    print("\n")

    horasTrabajadas_Martín=int(input("Introduzca las horas trabajadas por ese empleado: "))
    print("\n")

    pagoHora_Martín=float(input("Introduzca lo que gana el trabajador por hora: "))
    print("\n")

    # vamos a pensar que son trabajadores que trabajan 6 días de la semana por 1 d descanso

    sueldo_Martín=6*(pagoHora_Martín*horasTrabajadas_Martín)

    print("print el sueldo de ",nombreTrabajador_Martín," será: ",sueldo_Martín)
    print("\n")

    pagoTotal_Martín=pagoTotal_Martín +sueldo_Martín

    salida_Martín=int(input("Introduzca 0 para salir, otro número para continuar: "))
    print("\n")

print("La empresa pagará en total por ",contador_Martín," trabajadores: ",pagoTotal_Martín),