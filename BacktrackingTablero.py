# Función para generar el tablero con el nuevo esquema de valores
def generar_tablero(N):
    # Inicializamos el tablero vacío como una lista de listas
    tablero = [[0] * N for _ in range(N)]

    # Determinar el número de capas
    capas = (N + 1) // 2  # Se determina la cantidad de capas

    # Asignamos los valores a cada capa
    for capa in range(capas):
        # Calculamos los valores de la capa
        if capa == 0:
            # Capa más externa
            valor_vertice = 2
            valor_adyacente = 3
            valor_interno = 4
        elif capa == 1:
            # Segunda capa
            valor_vertice = 4
            valor_adyacente = 6
            valor_interno = 6
        else:
            # Capas internas
            valor_vertice = 8
            valor_adyacente = 8
            valor_interno = 8

        # Coordenadas del borde de la capa (el cuadrado de la capa)
        min_coord = capa
        max_coord = N - capa - 1

        # Asignamos los valores a las posiciones de la capa
        for i in range(min_coord, max_coord + 1):
            for j in range(min_coord, max_coord + 1):
                # Para la capa más externa, tratamos los vértices por separado
                if capa == 0:
                    if (i == min_coord and j == min_coord) or (i == min_coord and j == max_coord) or (i == max_coord and j == min_coord) or (i == max_coord and j == max_coord):
                        # Asignamos valor 2 a los vértices
                        tablero[i][j] = -valor_vertice
                    elif (i == min_coord and j == min_coord+1) or (i == min_coord and j == max_coord-1) or (i == max_coord-1 and j == min_coord) or (i == max_coord and j == max_coord-1) or (i == min_coord+1 and j == min_coord) or (i == min_coord+1 and j == max_coord) or (i == max_coord and j == min_coord+1) or (i == max_coord-1 and j == max_coord):
                        # Asignamos valor 3 a las celdas adyacentes a los vértices
                        tablero[i][j] = -valor_adyacente
                    else:
                        # Asignamos valor 4 al resto de las celdas
                        tablero[i][j] = -valor_interno
                else:
                    # Para las demás capas
                    if (i == min_coord or i == max_coord) and (j == min_coord or j == max_coord):
                        # Asignamos valor 4 a los vértices
                        tablero[i][j] = -valor_vertice
                    elif (i == min_coord or i == max_coord) or (j == min_coord or j == max_coord):
                        # Asignamos valor 6 a las celdas adyacentes a los vértices
                        tablero[i][j] = -valor_adyacente
                    else:
                        # Asignamos valor 6 al resto de las celdas
                        tablero[i][j] = -valor_interno

    return tablero

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(f'{x:2}' for x in fila))
    print()


N = 4
tablero = generar_tablero(N)
print(f"Tablero {N}x{N} con valores negativos:")
imprimir_tablero(tablero)