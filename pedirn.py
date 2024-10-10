#Vicente Y. Lopez V. - 240010
#mostrar la suma de los números ingresados.

total = 0
while True:
    try:
    
        num = int(input("Ingresa un número (o un numero negativo para salir): "))
        if num <0:
            break
        else:
            total += num
    except ValueError:
        print("Debes ingresar un número válido.")

print(f"La suma de los números ingresados es: {total}")