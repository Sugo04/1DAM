# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************************
# Ejercicio 18: Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el 
#               segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para determinar 
#               cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
# *******************************************************************************************************
#
import time

horas_Martín=0
minutos_Martín=0
segundos_Martín=0


salida_Martín=input("pulse cualquier tecla que no sea 0 para iniciar el contador(pulse CTRL+C para detener el bucle): ")

while salida_Martín!=0 :
    segundos_Martín=segundos_Martín+1
    
    if segundos_Martín==60:
        
        segundos_Martín=0
         
        
        minutos_Martín=minutos_Martín+1
        
        if minutos_Martín==60:
            minutos_Martín=0
        
            horas_Martín= horas_Martín+1
    
    #viendo que el contaador va a velocidades insanas, agregamos la función sleep de la librería time. 
    # Esta librería no ha salido de la nada, ha tocado informarnos por internet.
    
    time.sleep(1)
    print(horas_Martín,":", minutos_Martín,":", segundos_Martín)