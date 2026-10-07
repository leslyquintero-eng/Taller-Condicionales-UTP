num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 < num2:
    print(f"El número menor es: {num1}")
elif num2 < num1:
    print(f"El número menor es: {num2}")
else:
    print("Los dos números son iguales.")