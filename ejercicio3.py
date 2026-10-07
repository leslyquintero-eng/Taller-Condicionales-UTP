dia = input("Ingresa un día de la semana: ").strip().lower()

if dia == "lunes":
    print("¡Ánimo! Comenzando la semana con toda la energía.")
elif dia == "viernes":
    print("¡Por fin es viernes! Casi llega el fin de semana.")
elif dia == "sábado" or dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana! Tiempo de descansar.")
else:
    print("Día laboral/lectivo regular.")