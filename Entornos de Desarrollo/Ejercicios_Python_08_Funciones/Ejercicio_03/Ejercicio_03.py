# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 3: Crea una función que calcule la temperatura media de un día a partir de la
#              temperatura máxima y mínima. Luego, implementa un programa principal que,
#              utilizando la función anterior, solicite la temperatura máxima y mínima de
#              cada día y muestre la temperatura media. El programa pedirá el número de días.
# ****************************************************************************************

import TempMedia

tempMinMartín=int(input("Introduce la tempMin: "))
tempMaxMartín=int(input("Introduce la tempMax: "))

print(f"La temperatura media es: {TempMedia.media(tempMinMartín,tempMaxMartín)}")