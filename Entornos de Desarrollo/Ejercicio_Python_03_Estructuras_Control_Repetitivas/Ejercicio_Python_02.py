# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO************************************************
# Ejercicio 2: Crea una aplicación que permita adivinar un número. La aplicación genera 
#              un número aleatorio del 1 al 100. A continuación va pidiendo números y va
#              respondiendo si el número a adivinar es mayor o menor que el introducido,a 
#              demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
#              El programa termina cuando se acierta el número (además te dice en cuantos 
#              intentos lo has acertado), si se llega al limite de intentos te muestra el 
#              número que había generado.
# ******************************************************************************************
#
import random
# Mostramos con un mensaje en pantalla lo que el susuario deberá de hacer

print("Deberá de introducir número comprendidos entre 1 y 100 hasta acertar el que haya generdo la máquina.\n",
      "Si no lo adivina en 10 intentos, se mostrará la solución.")

# Generamos el valor aleatorio que se debe adivinar, con la función randint(), la cual nos 
# ha tocado investigar.

valor_aleatorio_martín = int(random.randint(1,100))

# Mostramos donde debe el usuario introducir el dato que está adivinando, utilizamos guess como intento.

guess_martín = int(input("Adivine el número ,entero, entre 1 y 100: "))

# Iniciamos un contador y mostramos soluciuón del problema.

i_martín = 1

if valor_aleatorio_martín== guess_martín:
     print("Acertaste")
else:
    while valor_aleatorio_martín!= guess_martín:
      i_martín=i_martín+1

      if i_martín<11:
            guess_martín = int(input("Adivine el número ,entero, entre 1 y 100: "))

      if i_martín>10: 
            print("No has adivinado el número. La solución era: ",valor_aleatorio_martín)
            break
                  
                  
    
     