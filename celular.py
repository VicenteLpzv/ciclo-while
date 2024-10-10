#Vicente Y. Lopez V. - 240010
#intentaremos desbloquear la pantalla

v=2
print ("Pantalla bloqueada")
p = str(input("Ingresar pin: "))

while p != "0705":
    
    print ("Pin incorrecto, intente nuevamente")
    print (f"le quedan {v} intentos")
    p = str(input("Ingresar pin: "))
    v -= 1
    if v == 0:
        print ("llamando a la policia")
        break

    
print ("Login correcto")
    
    
