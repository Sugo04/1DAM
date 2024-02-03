# Alumno: Héctor Martín Ortega
# 
# Curso 1º GS DAM
# 
# ********************************ENUNCIADO*****************************************
# Ejercicio 4: Suponiendo que hemos introducido una cadena por teclado que 
#              representa una frase (palabras separadas por espacios), realiza 
#              un programa que cuente cuantas palabras tiene.
# **********************************************************************************
#
# contadores son referidos por una única letra, para una comodidad de lectura de código (sinceramente no puedo mantenerme cuerdo leyendo i_apellido).

# obtenemos datos

caracter_Martín=str(input("aqui la cadena de palabras de la que desees conocer cuantas palabras tiene: "))

print("\n")

# incializamos contadores en 0
i=0
espacios=0

# realizamos el bucle para contar espacios y luego lo imprimimos (sumamos 1 por  que hay un espacio menso que palabras en la frase)
while i<len(caracter_Martín):
    
    if " "==caracter_Martín[i]:
        espacios=espacios+1
        
    i=i+1
        
print("Su cadena: ",caracter_Martín,". Está conformada por ", espacios+1, " palabras")