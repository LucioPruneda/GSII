r1 = 0
r2 = 0
i1 = 0
i2 = 0
totalVentas = 0
porcentaje1 = 0
porcentaje2 = 0
rTotal = 0
combo1 = 0 
combo2 = 0
ventamax=0
pedidos = int(input("Presione 1 para ingresar un pedido o cualquier otro numero para terminar: "))

while pedidos == 1:
    print("\n*****************************************************")
    print("*Combo1: café con leche con 2 medialunas + jugo $120*")
    print("*Combo2: infusión con tostadas, manteca y dulce $150*")
    print("*****************************************************\n")

    combo = int(input("Presione 1 para Combo1 o presione 2 para Combo2: "))

    if combo == 1:
        combo1 = 120
        print("Total a pagar: ", combo1)
        if combo1>ventamax:
            ventamax =combo1
        r1 += combo1
        i1 += 1
    elif combo == 2:
        combo2 = 150
        r2 += combo2
        i2 += 1
        print("Total a pagar: ", combo2)
        if combo2>ventamax:
            ventamax =combo2

    else:
        print("La opción ingresada no es correcta.")

    pedidos = int(input("Presione 1 para ingresar un pedido o cualquier otro numero para terminar: "))
    totalVentas += 1

rTotal = r1 + r2
porcentaje1 = i1 * 100 / totalVentas
porcentaje2 = i2 * 100 / totalVentas

print("\nTotal recaudado:", rTotal)   
print("Total de ventas:", totalVentas)
print("Total recaudado del Combo1:", r1)
print("Total recaudado del Combo2:", r2)
print("Del Combo1 se vendieron:", i1)
print("Del Combo2 se vendieron:", i2)
print("Porcentaje de ventas de Combo1:", porcentaje1)
print("Porcentaje de ventas de Combo2:", porcentaje2)
print("venta maxima fue", ventamax)
