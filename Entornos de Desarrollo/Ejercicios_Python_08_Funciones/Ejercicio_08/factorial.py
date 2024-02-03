def factorial(num1Martín):
    # Calcula el factorial de un número utilizando recursión porque sino da 0
    if num1Martín == 1 or num1Martín == 0:
        return 1
    else:
        return num1Martín * factorial(num1Martín - 1)
