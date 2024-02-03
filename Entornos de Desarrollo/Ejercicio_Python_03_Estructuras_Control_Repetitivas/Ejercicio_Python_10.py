# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************************
# Ejercicio 10: Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
# **********************************************************************************************
#

# mostramos en pantalla lo que vamos a hacer

print("Se le mostrará las tablas de multiplicar del 1, 2, 3, 4 y 5.")

# realizamos dos contadores
i_martín=0


while i_martín<5:
    i_martín=i_martín+1
    j_martín=0
    while j_martín<10:
        j_martín=j_martín+1
        multiplicación_martín=i_martín*j_martín
        print(i_martín,"*",j_martín, " es igual a: ", multiplicación_martín)
        if j_martín==10:
            print("\n")





