# Diagramas de Flujo - Taller Condicionales


## Ejercicio 1
```mermaid
graph TD
    A([Inicio]) --> B[/Leer numero/]
    B --> C{numero == 30}
    C -- Sí --> D[/Imprimir 'Ganaste un premio'/]
    C -- No --> E[/Imprimir 'Perdiste'/]
    D --> F([Fin])
    E --> F
```

## Ejercicio 2
```mermaid
graph TD
    A([Inicio]) --> B[/Leer num1, num2/]
    B --> C{num1 < num2}
    C -- Sí --> D[/Mostrar num1 es menor/]
    C -- No --> E{num2 < num1}
    E -- Sí --> F[/Mostrar num2 es menor/]
    E -- No --> G[/Mostrar son iguales/]
    D --> H([Fin])
    F --> H
    G --> H
```

## Ejercicio 3
```mermaid
graph TD
    A([Inicio]) --> B[/Leer dia/]
    B --> C{dia == 'lunes'}
    C -- Sí --> D[/Mensaje Lunes/]
    C -- No --> E{dia == 'viernes'}
    E -- Sí --> F[/Mensaje Viernes/]
    E -- No --> G{dia == 'sabado' o 'domingo'}
    G -- Sí --> H[/Mensaje Fin de semana/]
    G -- No --> I[/Mensaje Otro dia/]
    D --> J([Fin])
    F --> J
    H --> J
    I --> J
```

## Ejercicio 4
```mermaid
graph TD
    A([Inicio]) --> B[/Leer num/]
    B --> C{num < 0}
    C -- Sí --> D[valor_absoluto = num * -1]
    C -- No --> E[valor_absoluto = num]
    D --> F[/Mostrar valor_absoluto/]
    E --> F
    F --> G([Fin])
```

## Ejercicio 5
```mermaid
graph TD
    A([Inicio]) --> B[/Leer anio/]
    B --> C{anio % 4 == 0 y anio % 100 != 0 O anio % 400 == 0}
    C -- Sí --> D[/Imprimir 'Es bisiesto'/]
    C -- No --> E[/Imprimir 'NO es bisiesto'/]
    D --> F([Fin])
    E --> F
```

## Ejercicio 6
```mermaid
graph TD
    A([Inicio]) --> B[/Leer entrada/]
    B --> C{longitud de entrada != 1}
    C -- Sí --> D[/Mostrar mensaje de error/]
    C -- No --> E{letra esta en 'aeiou'}
    E -- Sí --> F[/Imprimir 'Es vocal'/]
    E -- No --> G[/Imprimir 'No es vocal'/]
    D --> H([Fin])
    F --> H
    G --> H
```

## Ejercicio 7
```mermaid
graph TD
    A([Inicio]) --> B[/Leer numero/]
    B --> C{numero % 3 == 0 y numero % 5 == 0}
    C -- Sí --> D[/Imprimir 'FizzBuzz'/]
    C -- No --> E{numero % 3 == 0}
    E -- Sí --> F[/Imprimir 'Fizz'/]
    E -- No --> G{numero % 5 == 0}
    G -- Sí --> H[/Imprimir 'Buzz'/]
    G -- No --> I[/Imprimir numero no es multiplo/]
    D --> J([Fin])
    F --> J
    H --> J
    I --> J
```

## Ejercicio 8
```mermaid
graph TD
    A([Inicio]) --> B[/Leer opcion A, B o C/]
    B --> C{opcion == 'A'}
    C -- Sí --> D[/Votó por partido rojo/]
    C -- No --> E{opcion == 'B'}
    E -- Sí --> F[/Votó por partido verde/]
    E -- No --> G{opcion == 'C'}
    G -- Sí --> H[/Votó por partido azul/]
    G -- No --> I[/Opcion erronea/]
    D --> J([Fin])
    F --> J
    H --> J
    I --> J
```

## Ejercicio 9
```mermaid
graph TD
    A([Inicio]) --> B[/Leer fecha 'dia, DD/MM'/]
    B --> C{¿Dia o fecha invalida?}
    C -- Sí --> D[/Mostrar Error/]
    C -- No --> E{¿Lunes, Martes o Miercoles?}
    E -- Sí --> F{¿Hubo examenes?}
    F -- Sí --> G[/Calcular % aprobados/]
    F -- No --> H[Fin Nivel]
    E -- No --> I{¿Jueves?}
    I -- Sí --> J{¿Asistencia > 50%?}
    J -- Sí --> K[/Asistió la mayoría/]
    J -- No --> L[/No asistió la mayoría/]
    I -- No --> M{¿Viernes y 1/1 o 1/7?}
    M -- Sí --> N[/Nuevo ciclo y calcular ingreso total/]
    M -- No --> H
    D --> O([Fin])
    G --> O
    H --> O
    K --> O
    L --> O
    N --> O
```