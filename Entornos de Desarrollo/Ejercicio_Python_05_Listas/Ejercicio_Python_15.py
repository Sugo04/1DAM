# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 15: Crear un programa de ordenador para gestionar los resultados de la quiniela
#              de fútbol. Para ello vamos a utilizar dos tablas:
# - Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los 
#   equipos de cada partido. En la quiniela se indican 15 partidos.
# - Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos 
#   columnas, en la primera se guarda el número de goles del equipo que está guardado en 
#   la primera columna de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa irá pidiendo los nombres de los equipos de cada partido y el resultado del 
# partido, a continuación se imprimirá la quiniela de esa jornada.
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados 
# de todas las jornadas de la temporada?: Habría que hacer una lista denominada "jornadaas"
# En la cual introdujeramos las tablas de los equipos y resultados según la jornada
# que se juega.
#
# ****************************************************************************************
#
equipos_Martín=[]
resultados_Martín=[]
for i in range(15):
    # Listas para almacenar los equipos y los resultados de cada partido
    partido_Martín = []
    resultado_Martín = []
    print("\n")
    # Bucle para las 15 columnas (equipos)
    for j in range(1):
        equipo1 = input("Introduce el nombre del equipo local: ")
        equipo2 = input("Introduce el nombre del equipo visitante: ")

        # Añadir equipos a la lista del partido, los separamos en dos diferentes, porque sino da problemas (solo lee un partido la respuesta)
        partido_Martín.append(equipo1)
        partido_Martín.append(equipo2)

        # Pedir y añadir resultados a la lista del resultado, los separamos en dos diferentes, porque sino da problemas (solo lee un partido la respuesta)
        golesEquipo1 = int(input("Introduce los goles del equipo local: "))
        golesEquipo2 = int(input("Introduce los goles del equipo visitante: "))
        resultado_Martín.append(golesEquipo1)
        resultado_Martín.append(golesEquipo2)

    # Añadir listas de equipos y resultados a las listas principales
    equipos_Martín.append(partido_Martín)
    resultados_Martín.append(resultado_Martín)

# supongo que con gestionar los resultados será mostrar quién gana, por ello realizamos un
# bucle que lea los datos.
print("--------------------------------QUINIELA----------------------------------------") 
for i in range(15):
    print(f"Partido {i + 1}: Se enfrentan {equipos_Martín[i][0]} y {equipos_Martín[i][1]} - Resultados: {resultados_Martín[i][0]} - {resultados_Martín[i][1]}")
print("--------------------------------QUINIELA----------------------------------------") 