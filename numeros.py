#Vicente Y. Lopez V. - 240010
#Leer 10 números e imprimir cuantos son positivos, 
# uantos negativos ycuantos cero

p = 0
ne = 0
c = 0

i=0
while i <= 9:
    n = int(input("Ingresa cualquier numero: "))
    i += 1
    if n > 0:
        p += 1
    elif n < 0:
        ne += 1
    else:
        c += 1
   
        
print (f"los positivos son {p} números")
print (f"los negativos son {ne} números")
print (f"los ceros son {c} números")
    
