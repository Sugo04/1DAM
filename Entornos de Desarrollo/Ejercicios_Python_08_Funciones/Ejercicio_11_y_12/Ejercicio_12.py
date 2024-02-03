# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 12: Mejora el ejercicio anterior creando una función para validar la fecha.
#               De tal forma que al leer una fecha se asegure que es válida.
# ****************************************************************************************


import Fechas

# Lee la fecha desde la función LeerFecha
diaMartín, mesMartín, añoMartín = Fechas.LeerFecha()

# Utiliza un bucle while para validar la fecha
while Fechas.ValidarFecha(diaMartín, mesMartín, añoMartín):
    # Imprime el día Juliano 
    print("Su día Juliano es:", Fechas.CalcularDiaJuliano(diaMartín, mesMartín, añoMartín))
