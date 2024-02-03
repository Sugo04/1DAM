def circunferencia(radioMartín):
    # Calcula el área y el perímetro de una circunferencia dados su radio.
    import math
    areaMartín = 2 * math.pi * math.pow(radioMartín, 2)
    perimetroMartín = 2 * math.pi * radioMartín
    return print(f"El área es: {round(areaMartín, 2)}\nEl perímetro es: {round(perimetroMartín, 2)}")
