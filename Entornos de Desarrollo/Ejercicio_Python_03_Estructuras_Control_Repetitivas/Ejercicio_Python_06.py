# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 6: Escribir un programa que imprima todos los números pares entre dos números que 
#              se le pidan al usuario.
# **********************************************************************************************
#

# Mostramos lo que el usuario debe de hacer con un mensaje en pantalla

print("introduzca dos números")

num1_martín= int(input("primer numero del intervalo: "))
num2_martín= int(input("segundo numero del intervalo: "))

# hacemos el bucle necesario

i_martín = num1_martín

while i_martín<num2_martín:
    i_martín=i_martín+1
    if i_martín%2==0:
        print(i_martín)
    