def LeerFecha():
    # Solicita al usuario que introduzca el día, mes y año, y devuelve la fecha.
    diaMartín = int(input("Introduce el día: "))
    mesMartín = int(input("Introduce el mes: "))
    añoMartín = int(input("Introduce el año: "))
    return diaMartín, mesMartín, añoMartín


def DiasDelMes(mesMartín, añoMartín):
    # Devuelve la cantidad de días en el mes especificado, considerando si el año es bisiesto.
    diasMesMartín = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (añoMartín % 4 == 0 and añoMartín % 100 != 0) or (añoMartín % 400 == 0):
        diasMesMartín[2] = 29
        return diasMesMartín[mesMartín]
    else:
        return diasMesMartín[mesMartín]


def EsBisiesto(añoMartín):
    # Verifica si el año especificado es bisiesto y muestra el resultado.
    if (añoMartín % 4 == 0 and añoMartín % 100 != 0) or (añoMartín % 400 == 0):
        return print("      -->", añoMartín, " es un año bisiesto")
    else:
        return print("      -->", añoMartín, " no es un año bisiesto")


def CalcularDiaJuliano(diaMartín, mesMartín, añoMartín):
    # Calcula el día juliano correspondiente a la fecha especificada.
    julianoMartín = 0
    for i in range(1, añoMartín):
        julianoMartín += DiasDelMes(1, i)
    julianoMartín += diaMartín
    return julianoMartín

def ValidarFecha(diaMartín, mesMartín, añoMartín):
    # Valida si la fecha especificada es válida.
    if diaMartín < 1 or diaMartín > DiasDelMes(mesMartín, añoMartín) or mesMartín < 1 or mesMartín > 12:
        return print("Fecha no válida."), False
    else:
        return True

