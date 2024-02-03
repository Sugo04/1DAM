# El nombre de cada funcion declara su proposito

def LeerFraccion():
    numeradorMartín = int(input("Ingrese el numerador: "))
    denominadorMartín = int(input("Ingrese el denominador: "))
    #utilizamos el mcd 
    mcdMartín = MCD(numeradorMartín, denominadorMartín)
    numeradorSimpMartín = numeradorMartín // mcdMartín
    denominadorSimpMartín = denominadorMartín // mcdMartín
    return numeradorSimpMartín, denominadorSimpMartín

def EscribirFraccion(fraccionMartín):
    numeradorMartín, denominadorMartín = fraccionMartín
    if denominadorMartín == 1:
        print(f"{numeradorMartín}")
    else:
        print(f"{numeradorMartín}/{denominadorMartín}")

def MCD(aMartín, bMartín):
    while bMartín:
        aMartín, bMartín = bMartín, aMartín % bMartín
    return aMartín

def SimplificarFuncion(fraccionMartín):
    numeradorMartín, denominadorMartín = fraccionMartín
    mcdSimpl = MCD(numeradorMartín, denominadorMartín)
    numeradorSimplificadoMartín = numeradorMartín // mcdSimpl
    denominadorSimplificadoMartín = denominadorMartín // mcdSimpl
    return numeradorSimplificadoMartín, denominadorSimplificadoMartín

def SumarFracciones(fraccion1Martín, fraccion2Martín):
    n1Martín, d1Martín = fraccion1Martín
    n2Martín, d2Martín = fraccion2Martín
    numeradorMartín = n1Martín * d2Martín + d1Martín * n2Martín
    denominadorMartín = d1Martín * d2Martín
    return SimplificarFuncion((numeradorMartín, denominadorMartín))

def RestarFracciones(fraccion1Martín, fraccion2Martín):
    n1Martín, d1Martín = fraccion1Martín
    n2Martín, d2Martín = fraccion2Martín
    numeradorMartín = n1Martín * d2Martín - d1Martín * n2Martín
    denominadorMartín = d1Martín * d2Martín
    return SimplificarFuncion((numeradorMartín, denominadorMartín))

def MultiplicarFunciones(fraccion1Martín, fraccion2Martín):
    n1Martín, d1Martín = fraccion1Martín
    n2Martín, d2Martín = fraccion2Martín
    numeradorMartín = n1Martín * n2Martín
    denominadorMartín = d1Martín * d2Martín
    return SimplificarFuncion((numeradorMartín, denominadorMartín))

def DividirFracciones(fraccion1Martín, fraccion2Martín):
    n1Martín, d1Martín = fraccion1Martín
    n2Martín, d2Martín = fraccion2Martín
    numeradorMartín = n1Martín * d2Martín
    denominadorMartín = d1Martín * n2Martín
    return SimplificarFuncion((numeradorMartín, denominadorMartín))
