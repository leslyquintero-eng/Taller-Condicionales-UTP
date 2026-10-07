opcion = input("Elija un candidato para votar (A: Rojo, B: Verde, C: Azul): ").strip().upper()

if opcion == "A":
    print("Usted ha votado por el partido rojo")
elif opcion == "B":
    print("Usted ha votado por el partido verde")
elif opcion == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")