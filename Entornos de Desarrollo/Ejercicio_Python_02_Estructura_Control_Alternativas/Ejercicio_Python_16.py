# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************
# Ejercicio 16: La política de cobro de una compañía telefónica es: cuando se realiza
#               una llamada, el cobro es por el tiempo que ésta dura, de tal forma que
#               los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 
#               céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo 
#               minuto, 50 céntimos.
#               Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, 
#               en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo 
#               para determinar cuánto debe pagar por cada concepto una persona que realiza 
#               una llamada.
# *******************************************************************************************
#

# Mostramos un mensaje en pantalla informando al usuario de lo que deberá de hacer

print("Introduzca el tiempo que ha durado la llamada en minutos y el dia de cuando la hizo.\n ",
      "para saber cuanto se le cobrará.")

# Con un mensaje indicamos donde debe introducir las variables.

minutos= int(input("Introdúce aquí los minutos con un número sin decimales: "))

dia = int(input("Introduzca un número entero entre 1 y 7 para indicar el día (1 siendo lunes y 7 domingo): "))

horario= int(input("Introduzca si fue por la mañana o la tarde; 1 para mañana y 2 para tarde: "))
# realizamos los condicionales necesarios para minutos y dia separadamente.
if minutos<= 5:
    
    precio_inicial= 1
elif minutos>5 and minutos<9:
     precio_inicial= float(((minutos-5)*0.8)+1)
     
elif minutos>8 and minutos<11:
    precio_inicial= float(((minutos-8)*0.7)+((minutos-5)*0.8)+1)

elif minutos>10:
    precio_inicial= float(((minutos - 10)*0.5) + ((minutos-8)*0.7)+((minutos-5)*0.8)+1)

else:
    
    print(" introdujo mal el tiempo")
    
if dia == 7:
    
    precio_total = float(precio_inicial*1.03)
    
else:
    if horario == 1:
        
         precio_total = float(precio_inicial*1.15)
         
    elif horario == 2:
        
         precio_total = float(precio_inicial*1.10)
    else:
        print("Introduciste mal la hora.")
        
# Mostramos la solución con un mensaje a pantalla

print(" Se le cobrará un total de ", precio_total, " euros por su llamada.")