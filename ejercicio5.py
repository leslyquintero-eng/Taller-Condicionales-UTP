anio = int(input("Ingresa un año: "))

# Es divisible por 4 y no por 100, excepto si es divisible por 400
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} NO es bisiesto.")