def LongitudPila(pilaMartín):
    # Retorna la longitud de la pila
    return len(pilaMartín)

def EstaVaciaPila(pilaMartín):
    # Verifica si la pila está vacía
    return len(pilaMartín) == 0

def EstaLlenaPila(pilaMartín):
    # Verifica si la pila está llena (la implementación actual siempre devuelve False)
    return len(pilaMartín) == len(pilaMartín)

def AddPila(cadMartín, pilaMartín):
    # Agrega un elemento a la pila
    return pilaMartín.append(cadMartín)

def SacarDeLaPila(pilaMartín):
    # Saca el último elemento de la pila (si no está vacía)
    if not EstaVaciaPila(pilaMartín):
        return pilaMartín.pop(len(pilaMartín)-1)
    else:
        print("La pila está vacía")
        return ""

def EscribirPila(pilaMartín):
    # Imprime todos los elementos de la pila
    for elem in pilaMartín:
        print(elem, end=" ")
    print()
