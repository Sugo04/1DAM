# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 20: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros 
# y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 
# 20 céntimos o 10 céntimos).
# **********************************************************************************
#

# Mostramos en un mensaje en la pantalla lo que debe de hacer el usuario.

print("Deberá de introducir la cantidad de cada tipo de moneda que tenga encima,",
      "no se contará el dinero que tengas en billetes o digital ")

# Mostramos con un mensaje dónde debe de introducir los datos

mon_2= int(input("Introduce la cantidad de monedas de 2 euros que tengas: "))

mon_1= int(input("Introduce la cantidad de monedas de 1 euro que tengas: "))

mon_50= int(input("Introduce la cantidad de monedas de 50 céntimos que tengas: "))

mon_20= int(input("Introduce la cantidad de monedas de 20 céntimos que tengas: "))

mon_10= int(input("Introduce la cantidad de monedas de 10 céntimos que tengas: "))

# Realizamos las operaciones convenientes y mostraremos la solución

mon2 = float(mon_2*2)
mon1 = float(mon_1*1)
mon50 = float(mon_50*0.5)
mon20 = float(mon_20*0.2)
mon10 = float(mon_10*0.1)

print("Tienes: ",float(mon2+mon1+mon10+mon20+mon50),"€")