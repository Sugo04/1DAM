# aunque se usen las mismas funciones que en el ejercicio anterior he decidido separarlos y nombrarlos 
# acorde a lo que trabajamos

def LongitudCola(colaMartín):
    # Retorna la longitud de la cola
    return len(colaMartín)

def EstaVaciaCola(colaMartín):
    # Verifica si la cola está vacía
    return len(colaMartín) == 0

def EstaLlenaCola(colaMartín):
    # Verifica si la cola está llena (la implementación actual siempre devuelve False)
    return len(colaMartín) == len(colaMartín)

def AddCola(cadMartín, colaMartín):
    # Agrega un elemento a la cola
    colaMartín.append(cadMartín)

def SacarDeLaCola(colaMartín):
    # Saca el primer elemento de la cola (si no está vacía)
    if not EstaVaciaCola(colaMartín):
        return colaMartín.pop(0)
    else:
        print("La cola está vacía")
        return ""

def EscribirCola(colaMartín):
    # Imprime todos los elementos de la cola
    for elem in colaMartín:
        print(elem, end=" ")
    print()
