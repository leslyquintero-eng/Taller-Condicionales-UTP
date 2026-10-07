# Entrada del usuario: "día, DD/MM"
entrada = input("Ingrese la fecha actual (formato 'día, DD/MM'): ").strip()

try:
    partes = entrada.split(",")
    dia_txt = partes[0].strip().lower()
    fecha_partes = partes[1].strip().split("/")
    
    dd = int(fecha_partes[0])
    mm = int(fecha_partes[1])

    dias_validos = ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]

    if dia_txt not in dias_validos or dd < 1 or dd > 31 or mm < 1 or mm > 12:
        print("Se produjo un error: Día de la semana o fecha fuera de rango válido.")
    else:
        # Lunes: inicial, Martes: intermedio, Miércoles: avanzado
        if dia_txt in ["lunes", "martes", "miércoles", "miercoles"]:
            hubo_examen = input("¿Se tomaron exámenes hoy? (si/no): ").strip().lower()
            if hubo_examen == "si" or hubo_examen == "sí":
                aprobados = int(input("Cantidad de alumnos aprobados: "))
                reprobados = int(input("Cantidad de alumnos reprobados: "))
                total = aprobados + reprobados
                if total > 0:
                    porcentaje = (aprobados / total) * 100
                    print(f"Porcentaje de aprobados: {porcentaje:.2f}%")
                else:
                    print("No hubo alumnos registrados.")
                    
        # Jueves: práctica hablada
        elif dia_txt == "jueves":
            asistencia = float(input("Ingrese el porcentaje de asistencia a clase (0-100): "))
            if asistencia > 50:
                print("Asistió la mayoría")
            else:
                print("No asistió la mayoría")
                
        # Viernes: inglés para viajeros
        elif dia_txt == "viernes":
            if dd == 1 and (mm == 1 or mm == 7):
                print("Comienzo de nuevo ciclo")
                cant_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                arancel = float(input("Ingrese el arancel en $ por alumno: "))
                ingreso_total = cant_alumnos * arancel
                print(f"Ingreso total: ${ingreso_total:.2f}")

except Exception:
    print("Se produjo un error en el formato de entrada. Asegúrese de usar 'día, DD/MM'.")