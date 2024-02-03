# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 11: El día juliano correspondiente a una fecha es un número entero que indica
#               los días que han transcurrido desde el 1 de enero del año indicado.
#               Queremos crear un programa principal que al introducir una fecha nos diga
#               el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
#               1. LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
#               2. DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
#               3. EsBisiesto: Recibe un año y nos dice si es bisiesto.
#               4. Calcular_Dia_Juliano: Recibe una fecha y nos devuelve el día juliano.
# ****************************************************************************************

import Fechas

# Lee la fecha desde la función LeerFecha
diaMartín, mesMartín, añoMartín = Fechas.LeerFecha()
dia_julianoMartín = Fechas.CalcularDiaJuliano(diaMartín, mesMartín, añoMartín)

# Imprime el resultado
print(f"Su día Juliano es: {dia_julianoMartín}")
