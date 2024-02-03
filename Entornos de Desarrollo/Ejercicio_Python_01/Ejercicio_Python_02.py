# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*******************************************
# Ejercicio 2: Calcular el perímetro y área de un rectángulo dada su base y su altura.
# ************************************************************************************
#


print("Recuerde que para que una figura sea rectangular, su base y altura " , 
      "deben de ser distintas. Si son iguales, será un cuadrado.")

base = float(input("Introduzca la medida (en cm) de la base del "+
                   "rectángulo que desea: "))

altura = float(input("Introduzca la medida (en cm) de la altura del "+
                     "rectángulo que desea:"))

# El área de un rectángulo es: base*altura

área = int(base*altura)
perímetro = int((2*base)+(2*altura))

print ("El área de su rectángulo será: ",área)

print("El perímetro del rectángulo será: ", altura)