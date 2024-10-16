#Vicente Y. Lopez V. - 240010
#calcule todas las ordenadas pares de la función
# Inicializamos la variable x en 0
x = 0

# Usamos un bucle while para recorrer los valores de x de 0 a 30
while x <= 30:
    # Calculamos el valor de la función Y = x^3 + 1
    y = x**3 + 1
    
    # Verificamos si y es un número par
    if y % 2 == 0:
        # Imprimimos la abscisa (x) y la ordenada (y)
        print(f"Abscisa: {x}, Ordenada: {y}")
    
    # Incrementamos x en 1 para la siguiente iteración
    x += 1

