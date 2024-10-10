#Vicente Y. Lopez V. - 240010
#calcule todas las ordenadas pares de la función
#Y=f(x)= x *x*x+1,

# Recorrer los valores de x desde 0 hasta 30
for x in range(31):
    # Calcular la ordenada Y usando la función dada
    Y = x * x * x + 1
    
    # Verificar si Y es par
    if Y % 2 == 0:
        # Imprimir la abscisa (x) y la ordenada (Y)
        print(f"Abscisa (x): {x}, Ordenada (Y): {Y}")
