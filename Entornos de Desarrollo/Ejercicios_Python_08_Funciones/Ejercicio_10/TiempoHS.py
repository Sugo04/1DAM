def segundos(horasMartín, minutosMartín, segundosMartín):
    # Convierte el tiempo a la cantidad total de segundos.
    return (horasMartín * 3600) + (minutosMartín * 60) + segundosMartín

def horaReal(segundosMartín):
    # Convierte la cantidad total de segundos a horas, minutos y segundos reales.
    horasMartín = segundosMartín / 3600
    minutosMartín = (segundosMartín % 3600) / 60
    secsMartín = (segundosMartín % 3600) % 60
    
    return round(horasMartín), round(minutosMartín), secsMartín
