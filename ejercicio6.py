entrada = input("Ingresa una letra: ")

if len(entrada) != 1:
    print("Error: No se puede procesar el dato. Debes ingresar solo un carácter.")
else:
    letra = entrada.lower()
    if letra in "aeiouáéíóú":
        print("Es vocal")
    else:
        print("No es una vocal")