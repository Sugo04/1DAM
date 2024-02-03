def mcd(num1Martín, num2Martín):
    # Calcula el máximo común divisor (MCD) utilizando el algoritmo de Euclides.
    if num1Martín % num2Martín == 0:
        return num2Martín
    else:
        return mcd(num2Martín, num1Martín % num2Martín)
