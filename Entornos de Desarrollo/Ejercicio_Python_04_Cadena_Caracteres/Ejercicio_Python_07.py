# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 7: Pide una cadena y dos caracteres por teclado (valida que sea 
#              un carácter), sustituye la aparición del primer carácter en la 
#              cadena por el segundo carácter.
# **********************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

#pedimos los datos
caracter_Martín=str(input("aqui la palabra o cadena de palabras de la que desees reemplazar un carácter: "))

letra_Martín=str(input("aquí la letra que deseas que sea reemplazada: "))
    
letra2_Martín= str(input("aquí la letra que deseas que reemplace a la otra letra: "))

# comprobamos que solo son un carácter y le hacemos repetir la introducción de datos en su caso
while len(letra_Martín)>1:
    letra_Martín=str(input("aquí la letra que deseas que sea reemplazada: "))
    
while len(letra2_Martín)>1:
    letra2_Martín=str(input("aquí la letra que deseas que reemplace a la otra letra: "))

i=0

# realizamos un bucle que compare las letras

while i<len(caracter_Martín):
    
    if letra_Martín==caracter_Martín[i]:
        j=i
    i=i+1
# imprimimos la solución sustituyendo los caracteres especificados

print(caracter_Martín.replace(caracter_Martín[j],letra2_Martín)) 
    