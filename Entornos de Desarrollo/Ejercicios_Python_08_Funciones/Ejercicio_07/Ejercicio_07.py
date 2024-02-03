# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 7: Crea una subrutina llamada "Login" que recibe un nombre de usuario y una
#              contraseña, y devuelve Verdadero si el nombre de usuario es “usuario1” y
#              la contraseña es “asdasd”. Además, recibe el número de intentos que se ha
#              intentado hacer login y si no se ha podido hacer login, incrementa este valor.
#              Crea un programa principal donde se pida un nombre de usuario y una
#              contraseña y se intente hacer login. Solamente hay tres oportunidades para
#              intentarlo.
# ****************************************************************************************


import Login

usuarioMartín=str(input("Introduce tu nombre de usuario: "))
contraseñaMartín=str(input("introduce la contraseña: "))

if Login.login(usuarioMartín,contraseñaMartín)==True:
    print(f"Binvenido {usuarioMartín}")
else:
    print("Intentelo de nuevo más tarde.")