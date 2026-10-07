num = float(input("Ingresa un número entero o real: "))

if num < 0:
    valor_absoluto = num * -1
else:
    valor_absoluto = num

print(f"El valor absoluto de {num} es: {valor_absoluto}")