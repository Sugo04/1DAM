# Alumno: Héctor Martín Ortega
#
# ****************************************************************************************
# Ejercicio 14: Crear un programa que lea los precios de 5 artículos y las cantidades 
#              vendidas por una empresa en sus 4 sucursales. Informar:
# - Las cantidades totales de cada artículo.
# - La cantidad de artículos en la sucursal 2.
# - La cantidad del artículo 3 en la sucursal 1.
# - La recaudación total de cada sucursal.
# - La recaudación total de la empresa.
# - La sucursal de mayor recaudación.
# ****************************************************************************************
#

#realizaremos una tabla para cada una de las siguientes cosas:
# cantidad, precios, vendido, sucursal, artículos
sucursales_Martín = ["sucursal 1", "sucursal 2", "sucursal 3", "sucursal 4"]
totalSucursal_Martín = []
cantidadTotalArticulo_Martín = []
articulos_Martín = []
precios_Martín = []

print("-------------------------------------------------------------------------------")

# Ingresar información de los artículos
for o in range(5):
    articulo = input("Introduce el nombre del artículo: ")
    articulos_Martín.append(articulo)
    precio = float(input("Indica el precio del artículo: "))
    precios_Martín.append(precio)
    print("\n")

print("-------------------------------------------------------------------------------")

# Ingresar información de las sucursales y ventas
for i in range(len(sucursales_Martín)):
    cantidades_Martín = []
    cantidadVendida_Martín = []
    totalesSucursal_Martín = []

    print("-", sucursales_Martín[i], "-")
    for j in range(5):
        print("-", articulos_Martín[j], "-")
        print("---------------------------------------------------------------------------------")

        cantidad = int(input("Indica la cantidad del artículo (no vendido) en su sucursal: "))
        cantidades_Martín.append(cantidad)

        vendido = int(input("Indica cuanto has vendido: "))
        cantidadVendida_Martín.append(vendido)
        print("---------------------------------------------------------------------------------")
        print("\n")

        cantidadTotalArticulo_Martín.append(cantidadVendida_Martín[j] + cantidades_Martín[j])
        totalesSucursal_Martín.append(cantidadVendida_Martín[j] * precios_Martín[j])

    totalSucursal_Martín.append(sum(totalesSucursal_Martín))

print("\n")
print("---------------------------------------------------------------------------------")

# Mostrar información
for u in range(5):
    print("La cantidad total de ", articulos_Martín[u], " es ", cantidadTotalArticulo_Martín[u])
    print("\n")

for e in range(len(sucursales_Martín)):
    total_art = sum(cantidadTotalArticulo_Martín[e * 5:(e + 1) * 5])
    print("El total de artículos en la ", sucursales_Martín[e], " son: ", total_art)
    print("\n")

print("En la ", sucursales_Martín[0], " la cantidad del tercer artículo es: ", cantidadTotalArticulo_Martín[2])
print("\n")

print("La empresa ha recaudado en total ", sum(totalSucursal_Martín), " euros.")
print("\n")
print("La sucursal con mayor recaudación es la ", sucursales_Martín[totalSucursal_Martín.index(max(totalSucursal_Martín))])
print("---------------------------------------------------------------------------------")