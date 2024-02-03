# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 7: Realizar una algoritmo que muestre la tabla de multiplicar de un número
#              introducido por teclado.
# **********************************************************************************************
#

# Mostramos lo que el usuario debe de hacer con un mensaje en pantalla

print("introduzca dos números")

num1_martín= int(input("primer numero del intervalo: "))

#inicializamos un contador y realizamos el bucle necesario

i_martín = 0

while i_martín<10:
    i_martín=i_martín+1
    print(num1_martín,"*",i_martín," es igual a :",num1_martín*i_martín)