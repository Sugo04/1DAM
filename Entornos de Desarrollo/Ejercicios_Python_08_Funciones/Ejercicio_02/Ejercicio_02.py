# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 2: Crea un programa que solicite dos números enteros al usuario y determine si
#              alguno de ellos es múltiplo del otro. Utiliza la función "EsMultiplo" que
#              recibe los dos números y devuelve True si el primero es múltiplo del segundo.
# ****************************************************************************************



import EsMultiplo 


# Solicitar dos números enteros al usuario
num1Martín = int(input("Introduce el primer número entero: "))
num2Martín = int(input("Introduce el segundo número entero: "))
   

# Verificar si alguno de los números es múltiplo del otro
if EsMultiplo.multiplo(num1Martín, num2Martín):
    print(f"Sí, {num1Martín} o {num2Martín} es múltiplo del otro.")
else:
    print(f"No, {num1Martín} y {num2Martín} no son múltiplos entre sí.")

