#Vicente Y. Lopez V. - 240010
#programa que permita al usuario ingresar los montos 
#de las compras de un cliente
d= 0
i = 0
while True:
    try:
        # Pedir el monto de la compra
        compra = float(input("Ingresa el monto de la compra (o '0' para salir): "))
        print (f"Ingresaste: {compra}")
        if compra == 0:
            break
        elif compra < 0:
            print("No se puede ingresar un monto negativo.")
           # continue
        else:
            i += compra
    except ValueError:
        print("Debes ingresar un número válido.")
print(f"El total de las compras es: {i}")   
if i >1000:
    d = (i * .10) 
    print(f"El total a pagar con descuento de: {d}. tu total será de {i - d}")  