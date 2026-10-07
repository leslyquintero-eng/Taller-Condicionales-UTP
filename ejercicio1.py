# Solicitamos el número al usuario
numero = float(input("Ingresa un número entre 10 y 50: "))

if numero == 30:
    print("Ganaste un premio")
else:
    print("Perdiste")

# ¿Qué pasaría si el usuario ingresa -10?
# Evaluación: La condición `numero == 30` resultará falsa (False), por lo que el programa ejecutará el bloque `else` e imprimirá "Perdiste".