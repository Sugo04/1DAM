# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 12: Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, 
#               si al final de cada mes deposita cantidades variables de dinero; además, se 
#               quiere saber cuánto lleva ahorrado cada mes.
# **********************************************************************************************
#

# Mostramos por un mensaje lo que debe de hacer el usuario

print("Vamos a comprobar cuanto ahorras a lo largo de 1 año, variando lo que ahorras por mes.")

# iniciamos un contador

i_martín=0
ahorro_total_martín=0
while  i_martín<12:

    i_martín=i_martín+1

    ahorro_mes_martín= float(input("Introduce lo que ahorras este mes: "))
    print("Este mes has ahorrado ",ahorro_mes_martín," euros")
    
    ahorro_total_martín=ahorro_total_martín+ahorro_mes_martín
    
print("Ahorrarás en total ",ahorro_total_martín," euros.")