# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************************
# Ejercicio 17: Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
#               Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo 
#               para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa 
#               por los N empleados.
# **********************************************************************************************************
#

# Mostramos un mensje especificando lo que se debde de hacer.

print("Deberá introducir el nombre de sus empleados, lo que cobra por hora, y las horas trabajadas. (Al día)",
      "Al final se le mostrará el pago total de su empresa a sus empleados.")
print("\n")

# colocamos una variable que nos servirá para salir del bucle.

salida_Martín=int(input("Introduzca 0 para salir, otro número para comenzar: "))
print("\n")

pagoTotal_Martín=0

contador_Martín=0

while salida_Martín!=0:

    contador_Martín=contador_Martín+1

    nombreTrabajador_Martín=str(input("Introduzca el nombre de su empleado: "))
    print("\n")

    i_martín=0
    horas_total_martín=0
    sueldo_Martín=float(input("Introduce lo que cobra por hora: "))
    print("\n")
    while  i_martín<6:

        i_martín=i_martín+1

        horas_día_martín= float(input("Introduce lo que ha trabajado este día: "))
        print("\n")
        
        horas_total_martín=horas_total_martín+horas_día_martín
        
    print(nombreTrabajador_Martín," obtendrá como sueldo esta semana ",horas_total_martín*sueldo_Martín," euros.")
    print("\n")

    salida_Martín=int(input("Introduzca 0 para salir, otro número para continuar: "))
    print("\n")

    pagoTotal_Martín=pagoTotal_Martín+(horas_total_martín*sueldo_Martín)

print("La empresa pagará en total por ",contador_Martín," trabajadores: ",pagoTotal_Martín)
print("\n")