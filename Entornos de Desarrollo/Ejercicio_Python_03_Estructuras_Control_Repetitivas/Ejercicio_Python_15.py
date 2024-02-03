# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************************
# Ejercicio 15: Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el 
#               segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar 
#               cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
# *******************************************************************************************************
#

# Mostramos con un mensaje lo que el usuario debe de hacer

print("Se le mostrará cuanto debe pagar mensualemnte durante 20 meses, y luego el total de lo que pagará.")

# declaramos contadores para un bucle.

contador_Martín = 1

pagoMes_Martín = 10

pagoTotal_Martín = 0

print("El mes ",contador_Martín," pagas: ",pagoMes_Martín)

while contador_Martín<19:

    contador_Martín= contador_Martín+1

    pagoMes_Martín=pagoMes_Martín*2

    print("El mes ",contador_Martín," pagas: ",pagoMes_Martín)

    pagoTotal_Martín=pagoTotal_Martín+pagoMes_Martín

print("pagarás en totañ: ",pagoTotal_Martín)   

