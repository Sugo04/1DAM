# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO**************************************************************
# Ejercicio 19: Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que 
#               seleccionamos la opción de “Salir”.
# *******************************************************************************************************
#

# Mostramos lo que el usuario debe de hacer.

print("Mire las opciones que le ofrece el menú")

# introducimos la variable que va a hacer que funcione nuestro código.

print(" Introduzca el número correpondiente a la opción que desea conocer:\n",
      "     1- Comer.\n",
      "     2- Beber.\n",
      "     3- Postres.\n",
      "     0- Salir del menú.\n",
      "Al salir del menú contacte con el camarero para tomar su pedido.\n")

opción_Martín=int(input("Introduzca aquí qué desea conocer (recuerde, 0 para salir del menú): "))
print("\n")

while opción_Martín!=0:

    if opción_Martín==1:

        print("Para comer podemos ofrecerle:\n",
              "- Chipirones.\n",
              "- Calamares a la romana.\n",
              "- Plato sorpresa de la casa.\n")
        
        print("\n")
        
        opción_Martín=int(input("Introduzca aquí la opción: "))
        print("\n")
        
    elif opción_Martín==2:

        print("Para beber podemos ofrecerle:\n",
              "- Vino: \n Tinto o Blanco\n",
              "- Agua.\n",
              "- Refresco: \n Cocacola o Fanta")
        print("\n")
        
        opción_Martín=int(input("Introduzca aquí la opción: "))
        print("\n")
        
    elif opción_Martín==3:
        
        print("Como postre podemos ofrecerle:\n",
              "- Tarta de queso.\n",
              "- Arroz con leche.\n",
              "- Natillas de la casa.\n")
        print("\n")
        
        opción_Martín=int(input("Introduzca aquí la opción: "))
        print("\n")

    else:

        print("instrucción no válida, introduzca un valor válido.\n")
        print("\n")
        opción_Martín=int(input("Introduzca aquí la opción: "))
        print("\n")