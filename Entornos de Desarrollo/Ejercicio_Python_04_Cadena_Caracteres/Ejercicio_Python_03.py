# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 3: Pide una cadena y un carácter por teclado (valida que sea un 
#              (carácter) y muestra cuantas veces aparece el carácter en la cadena.
# **********************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# Obtenemos datos
caracter_Martín=str(input("aqui la palabra o cadena de palabras de la que desees conocer cuantas veces se repite una letra: "))

letra_Martín=str(input("aquí la letra que deseas comprobar cuantas veces aparece: "))

# comprobamos que la letra sea solo 1 carácter
while len(letra_Martín)>1:
    letra_Martín=str(input("aquí la letra que deseas comprobar cuantas veces aparece:"))

#inicializamos contadores a 0

i=0
igual=0

# realizamos un bucle que cuente cuantas veces aparece el carácter y depués imprimimos la solución 
while i<len(caracter_Martín):
    
    if letra_Martín==caracter_Martín[i]:
        igual=igual+1
        
    i=i+1
        
print("La letra ",letra_Martín, " aparece ",igual," veces en la palabra: ",caracter_Martín)