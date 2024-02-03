# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO***********************************************
# Ejercicio 1: Escribir por pantalla cada carácter de una cadena introducida por teclado.
# ****************************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# pedimos datos
caracter_Martín=str(input("aqui la palabra o cadena de palabras: "))
print("\n")

# inicializamos los contadores
i=0
# ponemos una frase de decoración
print("Los caracteres que conforman tu palabra son: ")
print("\n")

# realizamos un bucle que imprima carácter a carácter
while i<len(caracter_Martín):
    
    print(caracter_Martín[i])
    i=i+1
    