numero = int(input("Ingresa un número entero: "))

# Se debe evaluar primero la condición conjunta (múltiplo de 3 y 5)
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print(f"El número {numero} no es múltiplo de 3 ni de 5.")