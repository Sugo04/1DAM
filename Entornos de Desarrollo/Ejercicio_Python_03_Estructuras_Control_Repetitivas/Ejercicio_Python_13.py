# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 13: Una empresa tiene el registro de las horas que trabaja diariamente un empleado 
#               durante la semana (seis días) y requiere determinar el total de éstas, así como 
#               el sueldo que recibirá por las horas trabajadas.
# **********************************************************************************************
#

# Mostramos por un mensaje lo que debe de hacer el usuario

print("Vamos a comprobar cuanto ahorras a lo largo de 1 año, variando lo que ahorras por mes.")

# iniciamos un contador y hacemos el bucle que da la solucion

i_martín=0
horas_total_martín=0
sueldo=float(input("introduce lo que cobras por hora: "))
while  i_martín<7:

    i_martín=i_martín+1

    horas_día_martín= float(input("Introduce lo que has trabajado hoy: "))
    
    horas_total_martín=horas_total_martín+horas_día_martín
    
print("Obtendrás como sueldo esta semana ",horas_total_martín*sueldo," euros.")