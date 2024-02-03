# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 02: Escribe un programa que lea una cadena y devuelva un diccionario con la 
#               cantidad de apariciones de cada carácter en la cadena.
# ****************************************************************************************
#
# (Solo agregamos el apellido a los diccionarios para mayor legibilidad. Además lo indica el enunciado.)

# colocamos una variable que lea la cadena propuesta por el usuario

cadena=str(input("Introduce la cadena que deseas conocer sus pariciones: ")) 

# inicializamos un diccionario vaciío donde se van a introducir los carácteres de nuestra cadena y como valor sus apariciones.

apariciónCarácter_Martín={}

# recorremos cada caracter dentro de la cadena y recogemos cuantas veces aparece

for caracter in cadena:
    apariciónCarácter_Martín[caracter] = cadena.count(caracter)
    
# mostramos la solución por cada uno de los carácteres de nuestra palabra, tomamos en cuenta que caracter es la variable y cantidad su 
#valor correpondiente en el diccionario.

print(f"cada uno de los caracteres de la palabra {cadena}, aparecen: ")

for caracter,cantidad in apariciónCarácter_Martín.items():
    print(f"{caracter}:{cantidad}")